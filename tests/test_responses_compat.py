import importlib.util
import asyncio
import json
from pathlib import Path
import unittest
from types import SimpleNamespace


path = Path(__file__).resolve().parents[1] / "runtimes/tabby/helpers/responses_compat.py"
spec = importlib.util.spec_from_file_location("responses_compat", path)
compat = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compat)


def chunk(delta=None, finish_reason=None, usage=None):
    value = {"model": "test-model", "choices": []}
    if delta is not None or finish_reason is not None:
        value["choices"] = [{"index": 0, "delta": delta or {}, "finish_reason": finish_reason}]
    if usage is not None:
        value["usage"] = usage
    return "data: " + json.dumps(value)


class ResponsesCompatibilityTests(unittest.TestCase):
    def events(self, chunks, body=None):
        return [json.loads(event) for event in compat.stream_chat_to_response(chunks, body or {"model": "test-model"})]

    def test_reasoning_streams_before_answer_and_retains_usage(self):
        usage = {"prompt_tokens": 80, "completion_tokens": 25, "total_tokens": 105,
                 "prompt_tokens_details": {"cached_tokens": 64}}
        events = self.events([chunk({"reasoning_content": "Check the constraints. "}),
                              chunk({"reasoning_content": "Choose a simple answer."}),
                              chunk({"content": "The answer."}), chunk(finish_reason="stop"),
                              chunk(usage=usage), "[DONE]"])
        types = [event["type"] for event in events]
        self.assertLess(types.index("response.reasoning_text.delta"), types.index("response.output_text.delta"))
        final = events[-1]["response"]
        self.assertEqual(final["output_text"], "The answer.")
        self.assertEqual(final["output"][0]["content"][0]["text"], "Check the constraints. Choose a simple answer.")
        self.assertEqual(final["output"][0]["summary"], [])
        self.assertEqual(final["usage"], {"input_tokens": 80, "output_tokens": 25, "total_tokens": 105,
                                         "input_tokens_details": {"cached_tokens": 64}})
        self.assertEqual([e["sequence_number"] for e in events], list(range(len(events))))

    def test_reasoning_only_token_limit_is_incomplete_not_empty_success(self):
        events = self.events([chunk({"reasoning_content": "Still considering the problem."}),
                              chunk(finish_reason="length"),
                              chunk(usage={"prompt_tokens": 10, "completion_tokens": 256, "total_tokens": 266})])
        self.assertEqual(events[-1]["type"], "response.incomplete")
        final = events[-1]["response"]
        self.assertEqual(final["status"], "incomplete")
        self.assertEqual(final["incomplete_details"], {"reason": "max_output_tokens"})
        self.assertEqual(final["usage"]["output_tokens"], 256)
        self.assertEqual([item["type"] for item in final["output"]], ["reasoning"])

    def test_usage_survives_a_later_empty_chunk(self):
        events = self.events([chunk({"content": "ok"}), chunk(finish_reason="stop"),
                              chunk(usage={"prompt_tokens": 2, "completion_tokens": 1}), chunk(), "[DONE]"])
        self.assertEqual(events[-1]["response"]["usage"]["output_tokens"], 1)

    def test_reasoning_message_and_fragmented_tool_calls_keep_ids_and_indices(self):
        events = self.events([
            chunk({"reasoning_content": "Use the lookup tool."}),
            chunk({"tool_calls": [{"index": 0, "id": "call_1", "function": {"name": "lookup", "arguments": '{"key":'}}]}),
            chunk({"content": "Looking it up."}),
            chunk({"tool_calls": [{"index": 0, "function": {"arguments": '"value"}'}}]}),
            chunk(finish_reason="tool_calls"),
        ])
        final = events[-1]["response"]
        self.assertEqual([item["type"] for item in final["output"]], ["reasoning", "function_call", "message"])
        self.assertEqual(final["output"][1]["arguments"], '{"key":"value"}')
        self.assertEqual(final["output"][1]["call_id"], "call_1")
        for event in events:
            if "output_index" in event:
                item = final["output"][event["output_index"]]
                if "item_id" in event:
                    self.assertEqual(event["item_id"], item["id"])
                if "item" in event:
                    self.assertEqual(event["item"]["id"], item["id"])

    def test_custom_tool_round_trip_preserves_raw_input(self):
        body = {"model": "test-model", "tools": [{"type": "custom", "name": "patch"}]}
        events = self.events([chunk({"tool_calls": [{"index": 0, "id": "call_patch", "function": {
            "name": "patch", "arguments": '{"content":"sample patch"}'}}]}), chunk(finish_reason="tool_calls")], body)
        final = events[-1]["response"]
        self.assertEqual(final["output"][0]["type"], "custom_tool_call")
        self.assertEqual(final["output"][0]["input"], "sample patch")
        request = compat.responses_to_chat_payload({"input": [*final["output"], {
            "type": "custom_tool_call_output", "call_id": "call_patch", "output": "applied"}]})
        self.assertEqual(request["messages"][-1]["role"], "tool")
        self.assertEqual(request["messages"][-1]["tool_call_id"], "call_patch")

    def test_requests_keep_stream_state_independent(self):
        first, second = compat.ResponseStream({}), compat.ResponseStream({})
        first.feed(chunk({"reasoning_content": "first"}))
        second.feed(chunk({"content": "second"}))
        first_final = json.loads(first.finish()[-1])["response"]
        second_final = json.loads(second.finish()[-1])["response"]
        self.assertNotEqual(first_final["id"], second_final["id"])
        self.assertEqual(first_final["output_text"], "")
        self.assertEqual(second_final["output_text"], "second")
        self.assertEqual(len(first_final["output"]), 1)
        self.assertEqual(second_final["output"][0]["type"], "message")

    def test_stream_translation_requests_final_backend_usage(self):
        payload = compat.responses_to_chat_payload({"input": "question", "stream": True})
        self.assertEqual(payload["stream_options"], {"include_usage": True})
        self.assertNotIn("stream_options", compat.responses_to_chat_payload({"input": "question"}))

    def test_nonstreaming_retains_reasoning_and_token_limit_status(self):
        result = compat.chat_to_response_payload({"choices": [{"finish_reason": "length", "message": {
            "content": "answer", "reasoning_content": "reason"}}]}, {})
        self.assertEqual([item["type"] for item in result["output"]], ["reasoning", "message"])
        self.assertEqual(result["status"], "incomplete")

    def test_replayed_reasoning_does_not_reject_conversation_history(self):
        payload = compat.responses_to_chat_payload({"input": [
            {"type": "reasoning", "summary": [], "content": [{"type": "reasoning_text", "text": "reason"}]},
            {"type": "message", "role": "assistant", "content": [{"type": "output_text", "text": "answer"}]},
            {"type": "message", "role": "user", "content": "next question"}]})
        self.assertEqual([item["role"] for item in payload["messages"]], ["assistant", "user"])

    def test_normalized_tool_body_preserves_the_disconnect_channel(self):
        async def run():
            calls = []
            async def original():
                calls.append(True)
                return {"type": "http.disconnect"}
            request = SimpleNamespace(_receive=original)
            compat.replace_request_body(request, b'{"tools":[]}')
            self.assertEqual(await request._receive(), {
                "type": "http.request", "body": b'{"tools":[]}', "more_body": False})
            self.assertEqual(await request._receive(), {"type": "http.disconnect"})
            self.assertEqual(len(calls), 1)
        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
