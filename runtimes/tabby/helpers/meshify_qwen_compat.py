"""Adapt generic client instructions to the pinned Qwen chat template."""


def normalize_messages(messages):
    instructions = [m for m in messages if m.role in ('system', 'developer')]
    if not instructions:
        return messages
    # Qwen accepts a single leading system message. Preserve all instruction
    # blocks in their original order and leave user/tool/assistant turns intact.
    parts = []
    for message in instructions:
        from endpoints.OAI.types.chat_completion import ChatCompletionMessagePart
        if parts:
            parts.append(ChatCompletionMessagePart(text='\n\n'))
        if isinstance(message.content, list):
            parts.extend(message.content)
        elif message.content is not None:
            parts.append(ChatCompletionMessagePart(text=message.content))
    from endpoints.OAI.types.chat_completion import ChatCompletionMessage
    return [ChatCompletionMessage(role='system', content=parts)] + [
        m for m in messages if m.role not in ('system', 'developer')]


def normalize_template_vars(values):
    values = dict(values)
    if values.get('reasoning_effort') == 'high':
        values['reasoning_effort'] = 'xhigh'
    return values


def install(model, chat):
    original_roles = chat.normalize_message_roles
    original_vars = chat.resolve_template_vars

    def is_qwen():
        return getattr(getattr(model.container, 'model_dir', None), 'name', None) == 'qwen3.8-27b'

    def roles(data):
        original_roles(data)
        if is_qwen():
            data.messages = normalize_messages(data.messages)

    def template_vars(data, container):
        values = original_vars(data, container)
        return normalize_template_vars(values) if is_qwen() else values

    chat.normalize_message_roles = roles
    chat.resolve_template_vars = template_vars
