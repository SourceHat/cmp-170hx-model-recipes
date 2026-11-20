"""Responses API compatibility for TabbyAPI, without persisting conversations."""

import json
import time
import uuid
from typing import Any, Iterable


def _text_parts(value: Any) -> str:
    """Convert Responses text parts to one chat message string."""
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if not isinstance(value, list):
        raise ValueError("Responses input content must be text")
    chunks: list[str] = []
    for part in value:
        if isinstance(part, str):
            chunks.append(part)
            continue
        if not isinstance(part, dict):
            raise ValueError("Responses input content must be text")
        kind = part.get("type")
        if kind in ("input_text", "text", "output_text"):
            text = part.get("text")
            if text is not None:
                chunks.append(str(text))
            continue
        # This runtime is text-only.  Reject images instead of silently
        # dropping user data or writing it to a model log.
        if kind in ("input_image", "image_url", "output_image"):
            raise ValueError("Responses image input is not supported by this model")
        raise ValueError("Unsupported Responses content part")
    return "".join(chunks)


def _tool_call(item: dict[str, Any]) -> dict[str, Any]:
    call_id = str(item.get("call_id") or item.get("id") or f"call_{uuid.uuid4().hex[:24]}")
    nested = item.get("custom") if isinstance(item.get("custom"), dict) else item
    is_custom = item.get("type") == "custom_tool_call" or isinstance(item.get("custom"), dict)
    arguments = item.get("arguments", item.get("input", nested.get("input", "{}")))
    if is_custom and isinstance(arguments, str):
        # LiteLLM's custom-tool bridge wraps raw grammar content in a
        # ``content`` function argument before sending it to Chat Completions.
        try:
            parsed = json.loads(arguments)
        except (TypeError, ValueError):
            parsed = None
        if not isinstance(parsed, dict) or "content" not in parsed:
            arguments = json.dumps({"content": arguments}, separators=(",", ":"), ensure_ascii=False)
    if not isinstance(arguments, str):
        arguments = json.dumps(arguments, separators=(",", ":"), ensure_ascii=False)
    return {
        "id": call_id,
        "type": "function",
        "function": {
            "name": str(item.get("name") or nested.get("name") or ""),
            "arguments": arguments,
        },
    }


def _function_tool(tool: Any, index: int = 0) -> dict[str, Any] | None:
    """Coerce Responses/Chat tool dialects to Tabby's function-tool shape.

    LiteLLM and newer OpenAI clients can send custom tools either flat or under
    a ``custom`` member.  Tabby's request model accepts only ``type=function``;
    preserving the name and input schema lets the model still issue a normal
    function call without exposing an arbitrary command path.
    """
    if not isinstance(tool, dict):
        return None
    kind = tool.get("type")
    if isinstance(tool.get("function"), dict):
        function = tool["function"]
    elif kind in (None, "function"):
        function = tool
    elif kind in ("custom", "custom_tool"):
        nested = tool.get("custom")
        function = nested if isinstance(nested, dict) else tool
    else:
        # Hosted tools (web search, MCP, computer use, shell, etc.) have no
        # executor in the local model process.  They must not reach Tabby.
        return None

    is_custom = kind == "custom"
    name = function.get("name") or tool.get("name") or f"custom_tool_{index}"
    description = function.get("description") or tool.get("description") or ""
    parameters = function.get("parameters")
    if parameters is None:
        parameters = function.get("input_schema")
    if parameters is None:
        fmt = function.get("format")
        if isinstance(fmt, dict):
            parameters = fmt.get("schema") or fmt.get("parameters")
            definition = fmt.get("definition")
            if definition:
                syntax = str(fmt.get("syntax") or "")
                description = (
                    f"{description}\n\nFormat:\n```{syntax}\n{definition}\n```"
                )
    if not isinstance(parameters, dict):
        if is_custom:
            parameters = {
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string",
                        "description": f"The {name} content following the specified format",
                    }
                },
                "required": ["content"],
            }
        else:
            parameters = {"type": "object", "properties": {}}
    return {
        "type": "function",
        "function": {
            "name": str(name),
            "description": str(description),
            "parameters": parameters,
        },
    }


def _input_messages(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, str):
        return [{"role": "user", "content": value}]
    if not isinstance(value, list):
        raise ValueError("Responses input is required")

    messages: list[dict[str, Any]] = []
    pending_text: list[str] = []

    def flush_pending() -> None:
        if pending_text:
            messages.append({"role": "user", "content": "".join(pending_text)})
            pending_text.clear()

    for item in value:
        if isinstance(item, str):
            pending_text.append(item)
            continue
        if not isinstance(item, dict):
            raise ValueError("Responses input items must be objects")
        kind = item.get("type")
        if kind in (None, "message"):
            flush_pending()
            role = str(item.get("role") or "user")
            content = _text_parts(item.get("content", ""))
            messages.append({"role": role, "content": content})
        elif kind in ("input_text", "text"):
            pending_text.append(str(item.get("text") or ""))
        elif kind == "function_call_output":
            flush_pending()
            output = item.get("output", "")
            if not isinstance(output, str):
                output = json.dumps(output, separators=(",", ":"), ensure_ascii=False)
            messages.append({
                "role": "tool",
                "tool_call_id": str(item.get("call_id") or item.get("id") or ""),
                "content": output,
            })
        elif kind == "function_call":
            flush_pending()
            messages.append({
                "role": "assistant",
                "content": None,
                "tool_calls": [_tool_call(item)],
            })
        elif kind == "custom_tool_call":
            flush_pending()
            messages.append({
                "role": "assistant",
                "content": None,
                "tool_calls": [_tool_call(item)],
            })
        elif kind == "custom_tool_call_output":
            flush_pending()
            output = item.get("output", item.get("input", ""))
            if not isinstance(output, str):
                output = json.dumps(output, separators=(",", ":"), ensure_ascii=False)
            messages.append({
                "role": "tool",
                "tool_call_id": str(item.get("call_id") or item.get("id") or ""),
                "content": output,
            })
        elif kind in ("input_image", "image_url"):
            raise ValueError("Responses image input is not supported by this model")
        elif kind == "reasoning":
            # Reasoning output items may be replayed beside their assistant
            # message. The chat template consumes the message/tool history.
            continue
        else:
            raise ValueError("Unsupported Responses input item")
    flush_pending()
    return messages


def _tools(value: Any) -> list[dict[str, Any]] | None:
    if value is None:
        return None
    # A few OpenAI-compatible clients send one tool object instead of a list
    # when only one tool is registered.  Accept it at the compatibility
    # boundary so the strict Tabby request model still receives a list.
    if isinstance(value, dict):
        value = [value]
    if not isinstance(value, list):
        raise ValueError("Responses tools must be a list")
    result: list[dict[str, Any]] = []
    for index, tool in enumerate(value):
        normalized = _function_tool(tool, index)
        if normalized is not None:
            result.append(normalized)
    return result


def _tool_choice(value: Any) -> Any:
    """Normalize Responses and custom tool-choice objects for Chat Completions."""
    if value is None or isinstance(value, str):
        return value
    if not isinstance(value, dict):
        return "auto"
    kind = value.get("type")
    if kind == "function":
        nested = value.get("function") if isinstance(value.get("function"), dict) else value
        name = nested.get("name")
        return {"type": "function", "function": {"name": str(name)}} if name else "auto"
    if kind == "custom":
        nested = value.get("custom") if isinstance(value.get("custom"), dict) else value
        name = nested.get("name")
        return {"type": "function", "function": {"name": str(name)}} if name else "auto"
    # Namespace/hosted choices cannot be executed by this local listener.
    return "auto"


def _custom_tool_names(value: Any) -> set[str]:
    names: set[str] = set()
    if not isinstance(value, list):
        return names
    for tool in value:
        if not isinstance(tool, dict) or tool.get("type") != "custom":
            continue
        nested = tool.get("custom") if isinstance(tool.get("custom"), dict) else tool
        name = nested.get("name") or tool.get("name")
        if name:
            names.add(str(name))
    return names


def normalize_chat_payload(body: dict[str, Any]) -> dict[str, Any]:
    """Normalize a Chat Completions request before Tabby's Pydantic parser."""
    if not isinstance(body, dict):
        return body
    payload = dict(body)
    if "tools" in payload:
        payload["tools"] = _tools(payload.get("tools"))
        if not payload["tools"] and "tool_choice" in payload:
            payload["tool_choice"] = "none"
    if "tool_choice" in payload:
        payload["tool_choice"] = _tool_choice(payload.get("tool_choice"))
    # Some clients still send the legacy ``functions`` array alongside custom
    # tools.  Keep it intact; Tabby accepts it and it carries no executable code.
    return payload


def responses_to_chat_payload(body: dict[str, Any]) -> dict[str, Any]:
    """Translate one Responses request into a managed chat request."""
    if not isinstance(body, dict) or "input" not in body:
        raise ValueError("Responses input is required")
    messages = _input_messages(body.get("input"))
    instructions = body.get("instructions")
    if instructions:
        messages.insert(0, {"role": "system", "content": _text_parts(instructions)})
    if not messages:
        raise ValueError("Responses input is required")

    payload: dict[str, Any] = {
        "messages": messages,
        # The supervised profile owns the loaded checkpoint.  Do not pass the
        # client model name into Tabby's inline model loader.
        "model": None,
        "stream": bool(body.get("stream", False)),
        "add_generation_prompt": True,
    }
    if payload["stream"]:
        payload["stream_options"] = {"include_usage": True}
    field_map = {
        "max_output_tokens": "max_tokens",
        "temperature": "temperature",
        "top_p": "top_p",
        "stop": "stop",
        "user": "user",
        "parallel_tool_calls": "parallel_tool_calls",
    }
    for source, target in field_map.items():
        if source in body and body[source] is not None:
            payload[target] = body[source]
    if "tools" in body:
        payload["tools"] = _tools(body.get("tools"))
        if not payload["tools"] and "tool_choice" in body:
            payload["tool_choice"] = "none"
    if "tool_choice" in body and body["tool_choice"] is not None:
        payload["tool_choice"] = _tool_choice(body["tool_choice"])
    if body.get("reasoning") is not None:
        payload["reasoning"] = body["reasoning"]
    text = body.get("text")
    if isinstance(text, dict) and isinstance(text.get("format"), dict):
        fmt = text["format"]
        kind = fmt.get("type")
        if kind == "json_schema":
            payload["response_format"] = {
                "type": "json_schema",
                "json_schema": fmt.get("schema") or {"type": "object"},
            }
        elif kind in ("json_object", "json"):
            payload["response_format"] = {"type": "json"}
    return payload


def _usage(usage: Any) -> dict[str, Any] | None:
    if usage is None:
        return None
    if hasattr(usage, "model_dump"):
        usage = usage.model_dump(mode="json", exclude_none=True)
    if not isinstance(usage, dict):
        return None
    prompt = int(usage.get("prompt_tokens") or 0)
    completion = int(usage.get("completion_tokens") or 0)
    result: dict[str, Any] = {
        "input_tokens": prompt,
        "output_tokens": completion,
        "total_tokens": int(usage.get("total_tokens") or prompt + completion),
    }
    cached = usage.get("prompt_tokens_details", {}).get("cached_tokens") if isinstance(usage.get("prompt_tokens_details"), dict) else None
    if cached is not None:
        result["input_tokens_details"] = {"cached_tokens": int(cached)}
    return result


def chat_to_response_payload(chat_response: Any, request_body: dict[str, Any], response_id: str | None = None) -> dict[str, Any]:
    """Translate a ChatCompletionResponse into an OpenAI response object."""
    if hasattr(chat_response, "model_dump"):
        chat_response = chat_response.model_dump(mode="json", exclude_none=True)
    choice = (chat_response.get("choices") or [{}])[0]
    message = choice.get("message") or {}
    text = message.get("content") or ""
    output: list[dict[str, Any]] = []
    reasoning = message.get("reasoning_content") or ""
    if reasoning:
        output.append({
            "id": f"rs_{uuid.uuid4().hex[:24]}", "type": "reasoning",
            "summary": [], "content": [{"type": "reasoning_text", "text": reasoning}],
            "status": "completed",
        })
    tool_calls = message.get("tool_calls") or []
    custom_names = _custom_tool_names(request_body.get("tools"))
    if text or not (tool_calls or reasoning):
        output.append({
            "id": f"msg_{uuid.uuid4().hex[:24]}",
            "type": "message",
            "status": "completed",
            "role": "assistant",
            "content": [{"type": "output_text", "text": text, "annotations": []}],
        })
    for call in tool_calls:
        function = call.get("function") or {}
        name = str(function.get("name") or "")
        call_id = str(call.get("id") or f"call_{uuid.uuid4().hex[:24]}")
        arguments = function.get("arguments") or "{}"
        if name in custom_names:
            try:
                parsed = json.loads(arguments) if isinstance(arguments, str) else arguments
            except (TypeError, ValueError):
                parsed = None
            if isinstance(parsed, dict) and "content" in parsed:
                custom_input = str(parsed["content"])
            else:
                custom_input = arguments if isinstance(arguments, str) else json.dumps(arguments, separators=(",", ":"))
            output.append({
                "id": str(call.get("id") or f"ctc_{uuid.uuid4().hex[:24]}"),
                "type": "custom_tool_call",
                "status": "completed",
                "call_id": call_id,
                "name": name,
                "input": custom_input,
            })
        else:
            output.append({
                "id": str(call.get("id") or f"fc_{uuid.uuid4().hex[:24]}"),
                "type": "function_call",
                "status": "completed",
                "call_id": call_id,
                "name": name,
                "arguments": arguments,
            })
    result: dict[str, Any] = {
        "id": response_id or f"resp_{uuid.uuid4().hex}",
        "object": "response",
        "created_at": int(time.time()),
        "status": "completed",
        "model": chat_response.get("model") or request_body.get("model") or "local-model",
        "output": output,
        "output_text": text,
        "parallel_tool_calls": request_body.get("parallel_tool_calls", True),
        "store": False,
    }
    usage = _usage(chat_response.get("usage"))
    if usage is not None:
        result["usage"] = usage
    if request_body.get("instructions") is not None:
        result["instructions"] = request_body["instructions"]
    if choice.get("finish_reason") == "length":
        result["status"] = "incomplete"
        result["incomplete_details"] = {"reason": "max_output_tokens"}
    return result


def _stream_event(event_type: str, **values: Any) -> str:
    return json.dumps({"type": event_type, **values}, separators=(",", ":"), ensure_ascii=False)


def _stream_tool_deltas(
    deltas: Any,
    state: dict[int, dict[str, Any]],
    custom_names: set[str],
    allocate_output_index=None,
) -> list[str]:
    """Translate Chat Completions tool deltas into Responses events."""
    events: list[str] = []
    if not isinstance(deltas, list):
        return events
    for raw in deltas:
        if not isinstance(raw, dict):
            continue
        index = raw.get("index", 0)
        try:
            index = int(index)
        except (TypeError, ValueError):
            index = 0
        function = raw.get("function") if isinstance(raw.get("function"), dict) else {}
        entry = state.setdefault(index, {
            "id": str(raw.get("id") or f"call_{uuid.uuid4().hex[:24]}"),
            "name": "",
            "arguments": "",
        })
        if raw.get("id"):
            entry["id"] = str(raw["id"])
        if function.get("name"):
            entry["name"] = str(function["name"])
        argument_delta = function.get("arguments")
        if argument_delta is None:
            argument_delta = ""
        if not isinstance(argument_delta, str):
            argument_delta = json.dumps(argument_delta, separators=(",", ":"), ensure_ascii=False)
        custom = entry["name"] in custom_names
        entry.setdefault("custom", custom)
        entry.setdefault("item_id", f"ctc_{uuid.uuid4().hex[:24]}" if custom else f"fc_{uuid.uuid4().hex[:24]}")
        if "output_index" not in entry:
            entry["output_index"] = allocate_output_index() if allocate_output_index else index + 1
        if not entry.get("added"):
            entry["added"] = True
            item: dict[str, Any] = {
                "id": entry["item_id"],
                "type": "custom_tool_call" if custom else "function_call",
                "status": "in_progress",
                "call_id": entry["id"],
                "name": entry["name"],
            }
            item["input" if custom else "arguments"] = ""
            events.append(_stream_event("response.output_item.added", output_index=entry["output_index"], item=item))
        if argument_delta:
            entry["arguments"] += argument_delta
            events.append(_stream_event(
                "response.custom_tool_call_input.delta" if custom else "response.function_call_arguments.delta",
                item_id=entry["item_id"],
                output_index=entry["output_index"],
                delta=argument_delta,
            ))
    return events


def _finish_stream_tools(state: dict[int, dict[str, Any]], custom_names: set[str]) -> list[str]:
    events: list[str] = []
    for index in sorted(state):
        entry = state[index]
        custom = entry.get("name") in custom_names
        arguments = entry.get("arguments") or "{}"
        if custom:
            try:
                parsed = json.loads(arguments)
            except (TypeError, ValueError):
                parsed = None
            value = parsed.get("content", arguments) if isinstance(parsed, dict) else arguments
            events.append(_stream_event(
                "response.custom_tool_call_input.done",
                item_id=entry["item_id"], output_index=entry["output_index"], input=str(value),
            ))
            item = {
                "id": entry["item_id"], "type": "custom_tool_call", "status": "completed",
                "call_id": entry["id"], "name": entry["name"], "input": str(value),
            }
        else:
            events.append(_stream_event(
                "response.function_call_arguments.done",
                item_id=entry["item_id"], output_index=entry["output_index"], arguments=arguments,
            ))
            item = {
                "id": entry["item_id"], "type": "function_call", "status": "completed",
                "call_id": entry["id"], "name": entry["name"], "arguments": arguments,
            }
        events.append(_stream_event("response.output_item.done", output_index=entry["output_index"], item=item))
    return events


def _merge_stream_tools(last_chat: dict[str, Any], state: dict[int, dict[str, Any]]) -> None:
    if not state:
        return
    choices = last_chat.setdefault("choices", [{}])
    if not choices:
        choices.append({})
    message = choices[0].setdefault("message", {})
    message["tool_calls"] = [
        {
            "id": item["id"], "type": "function",
            "function": {"name": item.get("name", ""), "arguments": item.get("arguments", "{}") or "{}"},
        }
        for item in (state[index] for index in sorted(state))
    ]


class ResponseStream:
    """One request's ordered output items, reasoning, tools and final usage."""
    def __init__(self, request_body):
        self.body = request_body
        self.response_id = f"resp_{uuid.uuid4().hex}"
        self.sequence = 0
        self.model = request_body.get("model") or "local-model"
        self.outputs = []
        self.tool_state = {}
        self.custom_names = _custom_tool_names(request_body.get("tools"))
        self.text_item = self.reasoning_item = None
        self.text_parts = []
        self.reasoning_parts = []
        self.usage = None
        self.finish_reason = None

    def emit(self, event_type, **values):
        result = _stream_event(event_type, sequence_number=self.sequence, **values)
        self.sequence += 1
        return result

    def start(self):
        response = {"id": self.response_id, "object": "response", "created_at": int(time.time()),
                    "status": "in_progress", "model": self.model, "output": []}
        return [self.emit("response.created", response=response),
                self.emit("response.in_progress", response=response)]

    def allocate_tool_index(self):
        index = len(self.outputs)
        self.outputs.append({})
        return index

    def tool_events(self, events):
        result = []
        for encoded in events:
            event = json.loads(encoded)
            if "item" in event:
                self.outputs[event["output_index"]] = event["item"]
            event_type = event.pop("type")
            result.append(self.emit(event_type, **event))
        return result

    def feed(self, chunk):
        if chunk == "[DONE]":
            return []
        try:
            parsed = json.loads(chunk.removeprefix("data: ").strip())
        except (TypeError, ValueError):
            return []
        if not isinstance(parsed, dict):
            return []
        self.model = parsed.get("model") or self.model
        self.usage = parsed.get("usage") or self.usage
        events = []
        for choice in parsed.get("choices") or []:
            self.finish_reason = choice.get("finish_reason") or self.finish_reason
            delta = choice.get("delta") or {}
            reasoning = delta.get("reasoning_content") or ""
            if reasoning:
                if self.reasoning_item is None:
                    self.reasoning_item = {"id": f"rs_{uuid.uuid4().hex[:24]}", "type": "reasoning",
                                           "status": "in_progress", "summary": [], "content": []}
                    self.outputs.append(self.reasoning_item)
                    events.append(self.emit("response.output_item.added", output_index=len(self.outputs) - 1,
                                            item=self.reasoning_item))
                self.reasoning_parts.append(reasoning)
                events.append(self.emit("response.reasoning_text.delta", item_id=self.reasoning_item["id"],
                                        output_index=self.outputs.index(self.reasoning_item), content_index=0,
                                        delta=reasoning))
            text = delta.get("content") or ""
            if text:
                if self.text_item is None:
                    self.text_item = {"id": f"msg_{uuid.uuid4().hex[:24]}", "type": "message", "role": "assistant",
                                      "status": "in_progress", "content": []}
                    self.outputs.append(self.text_item)
                    index = len(self.outputs) - 1
                    events.append(self.emit("response.output_item.added", output_index=index, item=self.text_item))
                    events.append(self.emit("response.content_part.added", item_id=self.text_item["id"],
                                            output_index=index, content_index=0,
                                            part={"type": "output_text", "text": "", "annotations": [], "logprobs": []}))
                self.text_parts.append(text)
                events.append(self.emit("response.output_text.delta", item_id=self.text_item["id"],
                                        output_index=self.outputs.index(self.text_item), content_index=0,
                                        delta=text, logprobs=[]))
            events.extend(self.tool_events(_stream_tool_deltas(
                delta.get("tool_calls"), self.tool_state, self.custom_names, self.allocate_tool_index)))
        return events

    def finish(self):
        events = []
        text = "".join(self.text_parts)
        reasoning = "".join(self.reasoning_parts)
        status = "incomplete" if self.finish_reason == "length" else "completed"
        if self.reasoning_item is not None:
            index = self.outputs.index(self.reasoning_item)
            self.reasoning_item.update(status=status, content=[{"type": "reasoning_text", "text": reasoning}])
            events.append(self.emit("response.reasoning_text.done", item_id=self.reasoning_item["id"],
                                    output_index=index, content_index=0, text=reasoning))
            events.append(self.emit("response.output_item.done", output_index=index, item=self.reasoning_item))
        if self.text_item is not None:
            index = self.outputs.index(self.text_item)
            part = {"type": "output_text", "text": text, "annotations": [], "logprobs": []}
            self.text_item.update(status=status, content=[part])
            events.append(self.emit("response.output_text.done", item_id=self.text_item["id"], output_index=index,
                                    content_index=0, text=text, logprobs=[]))
            events.append(self.emit("response.content_part.done", item_id=self.text_item["id"], output_index=index,
                                    content_index=0, part=part))
            events.append(self.emit("response.output_item.done", output_index=index, item=self.text_item))
        events.extend(self.tool_events(_finish_stream_tools(self.tool_state, self.custom_names)))
        chat = {"model": self.model, "choices": [{"finish_reason": self.finish_reason, "message": {
            "content": text, "reasoning_content": reasoning}}], "usage": self.usage}
        _merge_stream_tools(chat, self.tool_state)
        final = chat_to_response_payload(chat, self.body, response_id=self.response_id)
        final["output"] = self.outputs
        final["output_text"] = text
        events.append(self.emit("response.incomplete" if status == "incomplete" else "response.completed", response=final))
        return events


def stream_chat_to_response(chunks: Iterable[str], request_body: dict[str, Any]):
    """Translate chat SSE with the same request-local state as the async route."""
    state = ResponseStream(request_body)
    yield from state.start()
    for chunk in chunks:
        if chunk == "[DONE]":
            break
        yield from state.feed(chunk)
    yield from state.finish()


def replace_request_body(request, encoded):
    original_receive = request._receive
    sent = False
    request._body = encoded

    async def receive():
        nonlocal sent
        if not sent:
            sent = True
            return {"type": "http.request", "body": encoded, "more_body": False}
        return await original_receive()

    request._receive = receive


def install(app: Any) -> None:
    """Register Responses routes on a Tabby FastAPI application."""
    from contextlib import suppress
    from fastapi import Depends, HTTPException, Request
    from fastapi.responses import JSONResponse
    from sse_starlette import EventSourceResponse

    from common import model
    from common.auth import check_api_key
    from common.model import check_model_container
    from common.networking import DisconnectHandler, get_sse_ping_interval, request_tag
    from endpoints.OAI.types.chat_completion import ChatCompletionRequest
    from endpoints.OAI.utils.chat_completion import (
        apply_chat_template,
        generate_chat_completion,
        stream_generate_chat_completion,
    )

    @app.middleware("http")
    async def normalize_chat_tools(request: Request, call_next):
        # The normal Chat Completions route is registered by Tabby itself and
        # validates the body before our Responses route runs.  Rewrite only the
        # JSON tool dialect, with no logging or persistence of request content.
        path = request.url.path.rstrip("/") or "/"
        if request.method == "POST" and path in (
            "/v1/chat/completions", "/chat/completions"
        ):
            try:
                raw = await request.body()
                body = json.loads(raw)
                if isinstance(body, dict) and ("tools" in body or "tool_choice" in body):
                    normalized = normalize_chat_payload(body)
                    encoded = json.dumps(normalized, separators=(",", ":"), ensure_ascii=False).encode()
                    replace_request_body(request, encoded)
            except (ValueError, TypeError, json.JSONDecodeError):
                pass
        return await call_next(request)

    async def handle(request: Request):
        try:
            body = await request.json()
            chat_body = responses_to_chat_payload(body)
            data = ChatCompletionRequest.model_validate(chat_body)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        except Exception as exc:
            raise HTTPException(status_code=400, detail="Invalid Responses request") from exc

        if not hasattr(request.state, "id"):
            request.state.id = f"resp-{uuid.uuid4().hex}"
        await check_model_container()
        model_path = model.container.model_dir
        if model.container.prompt_template is None:
            raise HTTPException(status_code=422, detail="Chat completions are disabled because a prompt template is not set.")
        prompt, embeddings = await apply_chat_template(data)
        disconnect_handler = DisconnectHandler(request, f"{request_tag(request)} responses")
        await disconnect_handler.poll()
        if data.stream:
            async def response_stream():
                source = stream_generate_chat_completion(
                    prompt, embeddings, data, request, model_path, disconnect_handler
                )
                state = ResponseStream(body)
                for event in state.start():
                    yield event
                try:
                    async for chunk in source:
                        if chunk == "[DONE]":
                            break
                        for event in state.feed(chunk):
                            yield event
                    for event in state.finish():
                        yield event
                finally:
                    with suppress(Exception):
                        await disconnect_handler.cleanup()

            return EventSourceResponse(response_stream(), ping=get_sse_ping_interval())
        try:
            response = await generate_chat_completion(
                prompt, embeddings, data, request, model_path, disconnect_handler
            )
            return JSONResponse(chat_to_response_payload(response, body))
        finally:
            with suppress(Exception):
                await disconnect_handler.cleanup()

    # LiteLLM builds the endpoint from an api_base ending in /v1.  Keep the
    # unprefixed alias for clients that provide a host-only api_base.
    app.add_api_route("/v1/responses", handle, methods=["POST"], dependencies=[Depends(check_api_key)])
    app.add_api_route("/responses", handle, methods=["POST"], dependencies=[Depends(check_api_key)])
