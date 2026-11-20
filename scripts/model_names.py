"""Reader-facing model identities; source IDs and measurements stay unchanged."""
import re

MODEL_NAMES = {
    'qwen27-orca-mtp3-native': 'Qwen3.8-27B Orca',
    'qwen-flash-next-mtp2-layer-split': 'Qwen3.8-Flash-Next',
    'mimo-flash-mtp1-tp3': 'MiMo-V2.6-Flash',
    'glm-5.3-flash-mtp1-tp3': 'GLM-5.3-Flash',
    'apex-abliterated-exl3-mtp1-tp3': 'Apex Flash 1 EXL3',
    'apex-abliterated-awq-dflash2-pp3-balanced': 'Apex Flash 1 AWQ',
    'deepseek-v41-flash-dspark5-tp3': 'DeepSeek V4.1 Flash TP3',
    'deepseek-v41-flash-1017-dspark5-tp4': 'DeepSeek V4.1 Flash 1017 TP4',
    'qwen3.8-27b-exl3': 'Qwen3.8-27B',
}


def display_names(text):
    replacements = (
        (r'Qwen 3\.8\s+27B', 'Qwen3.8-27B'),
        (r'(?<!Qwen3\.8-27B )\bOrca\b', 'Qwen3.8-27B Orca'),
        (r'\bFlash Next\b', 'Qwen3.8-Flash-Next'),
        (r'\bMiMo V2\.6 Flash\b|\bMiMo\b(?![-\w])', 'MiMo-V2.6-Flash'),
        (r'\bGLM Flash\b|\bGLM 5\.3 Flash\b', 'GLM-5.3-Flash'),
        (r'\bApex EXL3\b', 'Apex Flash 1 EXL3'),
        (r'\bApex AWQ\b', 'Apex Flash 1 AWQ'),
        (r'\bDeepSeek 1017\b', 'DeepSeek V4.1 Flash 1017'),
        (r'\bApex\b(?! Flash 1|[-\w])', 'Apex Flash 1'),
        (r'\bGLM\b(?![-\w])', 'GLM-5.3-Flash'),
        (r'\bDeepSeek\b(?! V4\.1|[-\w])', 'DeepSeek V4.1 Flash'),
    )
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text)
    return text
