# Contributing Recipes

Each selected configuration lives in `recipes/<profile-id>/` with:

- `README.md`: model source, hardware, setup, parameters, results and limits.
- `recipe.json`: a small machine-readable description, validated against `schemas/recipe.schema.json`.
- `config.yml` or `engine-config.json`: engine settings, with listener and model paths substituted at launch.
- `launch.sh`: the shared launch helper with explicit device selection.
- `benchmarks.json`: numerical measurements with context, concurrency, output budget and timing method.
- `evidence.json`: memory observations, precision audits, verification, quantization and source references.

Pin checkpoints by full revision and runtime sources by commit/image digest.
Keep accepted decode throughput separate from end-to-end throughput and cold
prefill. Label aggregate request rates, cached requests, driver/runtime changes
and any difference between benchmark cache geometry and the selected recipe.
Retain the source receipt and JSON pointer for each wave, the common decode
interval and its accepted-token count, and the full per-request arrays. Verify
cache hits before labeling a repeated prompt as cached.

Report the per-request context limit and shared KV pool separately. Do not
turn a configured slot count into a claim that all slots can reach maximum
context simultaneously. Do not describe an allocation/context check as a
quality benchmark or a measured speed at that context.

Keep deployment choices out of recipes: no fixed service ports, physical-slot
assignments, boot defaults or assumptions about other models running alongside
the recipe. Document hardware used for measurements as benchmark context.

Historical configurations and their distinct versions are indexed in
`archive/history/catalog.json`, with explicit evidence status, configuration
IDs and source receipts. Preserve exact artifacts and runtime pins where the
source retained them. Keep detailed waves, latency-based estimates, quoted
rate summaries and bounded checks separate. Do not transfer an earlier run's
result to a configuration that merely cites it. Coverage must account for
every included Meshify archive entry and any explicit publication exclusions.
The detailed Strata templates remain in `archive/<profile-id>/` and are linked
through `archive/catalog.json`. Record missing integration and measurements;
archival status does not imply support by the recipe launcher.
The article is maintained separately on the SourceHat website.

After changing a recipe, archive record or runtime:

```bash
python3 scripts/build_docs.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Keep weights, binaries, keys, private host identifiers and raw conversation
logs out of the repository. Credit the checkpoint publishers and runtime
authors. Retain third-party license notices on patches and extracted code.

Contribute original documentation/data under CC BY 4.0 and standalone code
under Apache-2.0, as scoped in [LICENSE](LICENSE). Attribute SourceHat when
reusing recipes, retain [NOTICE](NOTICE) and applicable upstream notices,
and identify changes to adapted material. Do not relicense upstream files.
