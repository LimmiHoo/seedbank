# === Stage 5: Текстовый поиск ===
# Project: SeedBank
from difflib import SequenceMatcher

def highlight_matches(text: str, pattern: str) -> str:
    """Подсвечивает в строке все вхождения pattern, без учёта регистра."""
    if not pattern:
        return text
    lowered = text.lower()
    pattern_lower = pattern.lower()
    start = 0
    length = len(pattern_lower)
    parts = []
    index = lowered.find(pattern_lower, start)
    while index != -1:
        parts.append(text[start:index])
        parts.append(f"\033[1m{text[index:index + length]}\033[0m")
        start = index + length
        index = lowered.find(pattern_lower, start)
    parts.append(text[start:])
    return "".join(parts)


def find_varieties(varieties, pattern: str) -> list:
    """Ищет сорта по текстовым полям без учёта регистра и подсвечивает совпадения."""
    if not pattern:
        return varieties
    results = []
    for variety in varieties:
        name = variety.get("name", "")
        culture = variety.get("culture", "")
        hay = f"{name} {culture}".lower()
        if pattern.lower() in hay:
            matched_name = highlight_matches(name, pattern)
            matched_culture = highlight_matches(culture, pattern)
            line = f"{matched_name} [{matched_culture}]"
            results.append(line)
    return results


if __name__ == "__main__":
    demo = [
        {"name": "Морковь Нанна", "culture": "Овощ"},
        {"name": "Помидор Бычье сердце", "culture": "Овощ"},
        {"name": "Пшеница Зерно", "culture": "Зерно"},
    ]
    for result in find_varieties(demo, "помидор"):
        print(result)
