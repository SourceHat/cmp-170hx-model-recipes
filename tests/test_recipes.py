import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, REPO / "scripts" / (name+".py"))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


launch = module("launch")
overlay = module("apply_overlay")
prepare = module("prepare_runtime")
docs = module("build_docs")


class RecipeTests(unittest.TestCase):
    def recipe(self, name):
        return json.loads((REPO / "recipes" / name / "recipe.json").read_text())

    def render(self, name, devices):
        return launch.render(self.recipe(name), devices=devices, runtime_root="/tmp/runtime with spaces",
                             model_path="/tmp/weights with spaces", draft_path="/tmp/draft with spaces",
                             engram_path="/tmp/nvme with spaces", source_model_path="/tmp/source with spaces",
                             output_dir="/tmp/output with spaces")

    def test_tabby_keeps_api_identity_and_cache_geometry(self):
        name = "apex-abliterated-exl3-mtp1-tp3"
        plan = self.render(name,"GPU-aa,GPU-bb,GPU-cc")
        config = json.loads(plan["artifacts"]["config.yml"])
        self.assertEqual(config["model"]["model_name"], self.recipe(name)["model"]["served_name"])
        self.assertEqual(config["model"]["cache_size"],1374976)
        self.assertEqual(config["model"]["autosplit_reserve"],[2560,2336,2848])
        self.assertEqual(config["draft_model"]["draft_num_tokens"],1)
        self.assertFalse(config["draft_model"]["dynamic_draft"])
        self.assertEqual(config["model"]["max_seq_len"],524288)
        self.assertTrue(config["model"]["tensor_parallel"])
        self.assertEqual(plan["environment"]["CUDA_VISIBLE_DEVICES"],"GPU-aa,GPU-bb,GPU-cc")
        self.assertEqual(len(plan["symlinks"]),1)

    def test_flash_uses_layer_split_and_host_ngrams(self):
        plan = self.render("qwen-flash-next-mtp2-layer-split","0,1")
        cfg = json.loads(plan["artifacts"]["config.yml"])
        self.assertFalse(cfg["model"]["tensor_parallel"])
        self.assertTrue(cfg["model"]["ngram_ram"])
        self.assertEqual(cfg["draft_model"]["draft_num_tokens"],2)
        self.assertEqual((cfg["network"]["host"],cfg["network"]["port"]),("127.0.0.1",8000))

    def test_standard_qwen_preserves_its_stock_output_budget(self):
        plan=self.render("qwen3.8-27b-exl3","0")
        self.assertNotIn("--output-chunk-tokens",plan["argv"])

    def test_documented_commands_are_copyable_and_launch_without_gpu_imports(self):
        catalog = json.loads((REPO / "catalog.json").read_text())
        for item in catalog["recipes"]:
            with self.subTest(recipe=item["id"]):
                recipe = self.recipe(item["id"])
                blocks = re.findall(r"```bash\n(.*?)\n```", docs.card(recipe), re.S)
                self.assertEqual(len(blocks), 2)
                download, serve = [shlex.split(block.replace("\\\n", "")) for block in blocks]
                self.assertEqual(download[:4], ["python3", "scripts/download_model.py", item["id"], "--directory"])
                self.assertEqual(len(download), 5)
                self.assertEqual(serve[:2], ["bash", f"recipes/{item['id']}/launch.sh"])
                self.assertIn("--dry-run", serve)
                result = subprocess.run(serve, cwd=REPO, capture_output=True, text=True, check=True)
                plan = json.loads(result.stdout)
                self.assertEqual(len(plan["environment"]["CUDA_VISIBLE_DEVICES"].split(",")), recipe["hardware"]["card_count"])

    def test_balanced_awq_keeps_precision_partition_and_literal_paths(self):
        plan = self.render("apex-abliterated-awq-dflash2-pp3-balanced","0,1,2")
        argv = plan["argv"]
        spec = json.loads(argv[argv.index("--speculative-config")+1])
        self.assertEqual(spec["kv_cache_dtype"],"int8_per_token_head")
        self.assertEqual(spec["num_speculative_tokens"],3)
        self.assertEqual(argv[argv.index("--model")+1],str(Path("/tmp/weights with spaces").resolve()))
        self.assertEqual(argv[argv.index("--kv-cache-dtype")+1],"fp8_e4m3")
        self.assertEqual(plan["environment"]["VLLM_PP_LAYER_PARTITION"],"17,15,13")
        self.assertEqual(argv[argv.index("--port")+1],"8000")

    def test_listener_defaults_and_overrides_reach_every_runtime(self):
        catalog = json.loads((REPO / "catalog.json").read_text())
        for item in catalog["recipes"]:
            recipe = self.recipe(item["id"])
            original = json.loads(json.dumps(recipe))
            for options, expected in [({}, ("127.0.0.1", 8000)),
                                      ({"host": "127.0.0.2", "port": 9001}, ("127.0.0.2", 9001))]:
                with self.subTest(recipe=item["id"], options=options):
                    plan = launch.render(recipe,
                                         devices=",".join(map(str,range(recipe["hardware"]["card_count"]))),
                                         runtime_root="/tmp/runtime", model_path="/tmp/model",
                                         draft_path="/tmp/draft", engram_path="/tmp/nvme",
                                         source_model_path="/tmp/source", **options)
                    runtime = recipe["runtime"]["id"]
                    if runtime == "tabby":
                        listener = json.loads(plan["artifacts"]["config.yml"])["network"]
                    elif runtime == "deepseek":
                        listener = {"host": plan["environment"]["BIND_ADDRESS"],
                                    "port": int(plan["environment"]["PORT"])}
                    else:
                        argv = plan["argv"]
                        listener = {"host": argv[argv.index("--host")+1],
                                    "port": int(argv[argv.index("--port")+1])}
                    self.assertEqual((listener["host"],listener["port"]), expected)
                    self.assertEqual(recipe,original)

    def test_deepseek_uses_dspark_and_separate_nvme_path(self):
        recipe = self.recipe("deepseek-v41-flash-dspark5-tp3")
        plan = self.render(recipe["id"],"0,1,2")
        argv=recipe["engine_config"]["argv"]
        spec=json.loads(argv[argv.index("--speculative-config")+1])
        self.assertEqual(spec["method"],"dspark")
        self.assertEqual(spec["num_speculative_tokens"],5)
        self.assertEqual(plan["argv"][:2],["docker","compose"])
        self.assertEqual(plan["environment"]["ENGRAM_DIR"],str(Path("/tmp/nvme with spaces").resolve()))
        self.assertEqual(plan["environment"]["SOURCE_MODEL_DIR"],str(Path("/tmp/source with spaces").resolve()))
        self.assertEqual(argv[argv.index("--tensor-parallel-size")+1],"3")
        self.assertEqual(argv[argv.index("--pipeline-parallel-size")+1],"1")

    def test_deepseek_cli_passes_assets_devices_and_listener_to_docker(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            executable = root / "docker"
            executable.write_text("#!/usr/bin/env python3\nimport json, os, sys\n"
                                  "keys = ('MODEL_DIR', 'SOURCE_MODEL_DIR', 'ENGRAM_DIR', 'DEVICES', 'BIND_ADDRESS', 'PORT')\n"
                                  "print(json.dumps({'argv':sys.argv[1:], 'environment':{key:os.environ[key] for key in keys}}))\n")
            executable.chmod(0o755)
            env = dict(os.environ, PATH=str(root)+os.pathsep+os.environ.get("PATH",""))
            command = ["bash", "recipes/deepseek-v41-flash-dspark5-tp3/launch.sh",
                       "--devices", "2,4,6", "--model-path", str(root/"TP3 weights"),
                       "--source-model-path", str(root/"source weights"),
                       "--engram-path", str(root/"NVMe tables"),
                       "--output-dir", str(root/"launch"), "--host", "127.0.0.2", "--port", "9001"]
            result = subprocess.run(command,cwd=REPO,env=env,capture_output=True,text=True,check=True)
            launched = json.loads(result.stdout)
            self.assertEqual(launched["argv"][:3],["compose","-f",str(REPO/"recipes/deepseek-v41-flash-dspark5-tp3/compose.yaml")])
            self.assertEqual(launched["environment"],{
                "MODEL_DIR":str(root/"TP3 weights"), "SOURCE_MODEL_DIR":str(root/"source weights"),
                "ENGRAM_DIR":str(root/"NVMe tables"), "DEVICES":"2,4,6", "BIND_ADDRESS":"127.0.0.2", "PORT":"9001"})

    def test_device_selection_is_exact(self):
        for devices in ["0,0", "0", "0,1,2", "0;"]:
            with self.assertRaises(ValueError):
                launch.selected_devices(devices,2)

    def test_paths_never_become_shell_commands(self):
        r=self.recipe("apex-abliterated-awq-dflash2-pp3-balanced")
        path="/tmp/$(touch never-execute)"
        plan=launch.render(r,devices="0,1,2",runtime_root="/tmp/r",model_path=path,draft_path=path,engram_path=path)
        self.assertEqual(plan["argv"][plan["argv"].index("--model")+1],str(Path(path).resolve()))

    def test_draft_paths_with_quotes_and_backslashes_remain_valid_json(self):
        recipe = self.recipe("apex-abliterated-awq-dflash2-pp3-balanced")
        draft = '/tmp/draft "quoted" \\weights'
        plan = launch.render(recipe, devices="0,1,2", runtime_root="/tmp/runtime",
                             model_path="/tmp/main", draft_path=draft)
        argv = plan["argv"]
        speculation = json.loads(argv[argv.index("--speculative-config") + 1])
        self.assertEqual(speculation["model"], str(Path(draft).resolve()))

    def test_prepare_pins_sources_and_sm80_without_loading_models(self):
        p=prepare.build_plan("tabby","/tmp/runtimes")
        self.assertEqual(p["environment"]["TORCH_CUDA_ARCH_LIST"],"8.0")
        checkouts=[c[-1] for c in p["commands"] if "--detach" in c]
        self.assertEqual(len(checkouts),2)
        self.assertTrue(all(len(x)==40 for x in checkouts))
        self.assertTrue(all("serve" not in c for c in p["commands"]))

    def test_overlay_installs_only_manifest_payloads(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp)/"packages"
            manifest=REPO/"runtimes/apex-awq/overlay-manifest.json"
            count=overlay.apply(manifest,target)
            data=json.loads(manifest.read_text())
            self.assertEqual(count,len(data["files"]))
            for row in data["files"]:
                self.assertEqual(hashlib.sha256((target/row["target"]).read_bytes()).hexdigest(),row["sha256"])

    def test_overlay_rejects_path_escape(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest=Path(tmp)/"bad.json"
            manifest.write_text(json.dumps({"files":[{"target":"../escape","file":"LICENSE","sha256":"0"*64}]}))
            with self.assertRaises(ValueError):overlay.apply(manifest,Path(tmp)/"packages")

    def test_overlay_preserves_a_hardlinked_base(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp)/"original.py"
            base.write_text("original package content\n")
            target=Path(tmp)/"packages"
            target.mkdir()
            os.link(base,target/"LICENSE")
            data={"files":[{"target":"LICENSE","file":"LICENSE","sha256":hashlib.sha256((REPO/"LICENSE").read_bytes()).hexdigest()}]}
            manifest=Path(tmp)/"manifest.json"
            manifest.write_text(json.dumps(data))
            overlay.apply(manifest,target)
            self.assertEqual(base.read_text(),"original package content\n")
            self.assertNotEqual(base.stat().st_ino,(target/"LICENSE").stat().st_ino)


if __name__=="__main__":
    unittest.main()
