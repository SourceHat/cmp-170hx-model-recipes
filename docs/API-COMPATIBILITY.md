# Completion, Chat And Responses Interfaces

The Tabby startup adapter retains the native `/v1/completions` and
`/v1/chat/completions` endpoints and adds `/v1/responses` (with a `/responses`
alias). It serves the selected checkpoint through the same generator and KV
pool; it does not create a second model instance or a request-wide mutex.

Independent requests can progress in the same batched decode iterations.
Prompt ingestion and decode are interleaved according to
[the mixed serving policy](MIXED-SERVING.md). A tool flow still waits for a
tool result before its next dependent model turn; separate flows can run
concurrently.

## Responses Streaming

Each request has its own output items and monotonically increasing event sequence
numbers. Streaming forwards reasoning as `response.reasoning_text.delta`, answer
text as `response.output_text.delta`, and function/custom-tool argument events.
Output-item IDs and indices remain consistent between the deltas, item-done
events and the final response.

Reasoning is represented as model-produced `reasoning_text`, with an empty
summary array. It is not relabeled as a generated reasoning summary. An agent
client should consume reasoning/tool events as well as answer-text events when
displaying progress; a reasoning phase may contain no answer text yet.

The adapter requests final upstream stream usage and retains it through the
terminal response. Total accepted output includes reasoning as reported by the
backend. A separate reasoning-token breakdown is only available when the
backend supplies it. Cached input counts remain distinct from total input.

Reaching the output-token limit produces `response.incomplete` and
`incomplete_details.reason = max_output_tokens`; normal completion produces
`response.completed`. Nonstreaming responses also retain reasoning and
token-limit status. Both forms normalize supported text, function and custom-tool
history. Replayed reasoning items do not become extra user messages.

## Deployment Scope

The routes use TabbyAPI's existing API-key dependency. Tool-schema normalization
preserves the original ASGI receive channel after forwarding the normalized body,
so client disconnects can cancel owned generation. The adapter does not persist
request/response content or implement hosted tools, image input, saved Responses
objects, or a stateful `previous_response_id` store. Supply the conversation
history explicitly for these recipes.

CPU tests cover request-state isolation, reasoning-only token-limit endings,
usage retention, fragmented function arguments, custom-tool round trips,
stable item identity/indexing and disconnect propagation. Reasoning/text/output
item events were also checked against the installed OpenAI SDK schemas.
The event definitions follow the
[official Responses streaming reference](https://developers.openai.com/api/docs/api-reference/responses-streaming).

Two simultaneous Qwen3.8-27B Orca Responses requests were checked through a LiteLLM gateway
under ordinary background traffic. Both streamed reasoning and answer text,
both reported their full 384 accepted output tokens, and their progress intervals
overlapped. A separate tool-bearing chat stream was closed after its first model
delta; the generator cancelled it after 14 tokens against a 512-token budget.
These live checks are in
[the separate verification data](../data/serving-scheduler-verification.json).
They are interface/concurrency checks, not isolated throughput benchmarks or
qualification of another operator's gateway availability/fallback policy.
