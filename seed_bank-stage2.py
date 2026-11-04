# === Stage 2: Проверка полей ===
# Project: SeedBank
import datetime


def normalize_seed_name(value):
    text = value.strip()
    if not text:
        raise ValueError("название сорта не может быть пустым")
    return text.title()


def normalize_culture(value):
    text = value.strip().lower()
    if not text:
        raise ValueError("культуру нельзя оставить пустой")
    if not (text.startswith(("ов", "о")) or text.startswith(("ыш", "ич", "ичн", "ниц", "ницн", "ицн"))) or text == "другое":
        raise ValueError("культура не распознана, ожидаются окончания: ов, о, ыш, ич, ично и т. п.")
    return text


_CULTURE_KEYWORDS = {"ов", "о", "ыш", "ич", "ичн", "ниц", "ницн", "ицн"}


def normalize_quantity(value):
    text = value.strip()
    try:
        number = int(text)
    except ValueError:
        raise ValueError("количество должно быть целым числом")
    if number <= 0:
        raise ValueError("количество семян должно быть больше нуля")
    return number


def normalize_expiry(value):
    text = value.strip()
    if not text:
        raise ValueError("срок годности не может быть пустым")
    try:
        date = datetime.datetime.strptime(text, "%d.%m.%Y").date()
    except ValueError:
        raise ValueError("срок годности должен быть в формате ДД.ММ.ГГГГ")
    return date


def validate_seed_name(name):
    normalized = normalize_seed_name(name)
    if len(normalized) > 50:
        raise ValueError("название сорта слишком длинное (не более 50 символов)")
    if len(normalized) < 1:
        raise ValueError("название сорта не может быть пустым")
    return normalized


def validate_culture(culture):
    normalized = normalize_culture(culture)
    if not normalized:
        raise ValueError("культура не может быть пустой")
    return normalized


def validate_quantity(quantity):
    normalized = normalize_quantity(quantity)
    if not isinstance(normalized, int) or normalized <= 0:
        raise ValueError("количество семян должно быть целым положительным числом")
    return normalized


def validate_expiry(expiry):
    normalized = normalize_expiry(expiry)
    if not isinstance(normalized, datetime.date):
        raise ValueError("срок годности должен быть датой")
    return normalized
