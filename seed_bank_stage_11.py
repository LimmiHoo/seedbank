# === Stage 11: Просмотр истории ===
# Project: SeedBank
import datetime


def parse_date(value):
    if not value:
        return None
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%Y/%m/%d"):
        try:
            return datetime.datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    return None


def format_date(value):
    if not value:
        return "-"
    return value.strftime("%d.%m.%Y")


def build_seed_record_line(record):
    name = record.get("name", "")
    culture = record.get("culture", "")
    quantity = record.get("quantity", 0)
    expiry = record.get("expiry", None)

    if culture:
        name_part = f"{name} ({culture})"
    else:
        name_part = name

    line = f"• {name_part} — {quantity} шт., срок годности: {format_date(expiry)}"
    return line


def history_block(record):
    name = record.get("name", "")
    culture = record.get("culture", "")

    if culture:
        title = f"Сорт: {name} ({culture})"
    else:
        title = f"Сорт: {name}"

    quantity = record.get("quantity", 0)
    expiry = record.get("expiry", None)
    added = record.get("added", None)

    details = []
    if quantity is not None:
        details.append(f"Количество: {quantity} шт.")
    if expiry is not None:
        details.append(f"Срок годности: {format_date(expiry)}")
    if added is not None:
        details.append(f"Добавлен: {format_date(added)}")

    body = "\n".join(details)
    return f"{title}\n{body}"


def render_seed_history(records):
    if not records:
        return "История пуста."
    lines = []
    for record in records:
        lines.append(history_block(record))
        lines.append("-" * 40)
    return "\n".join(lines)


if __name__ == "__main__":
    sample = [
        {
            "name": "Морковь Нант",
            "culture": "Овощи",
            "quantity": 50,
            "expiry": "2026-03-15",
            "added": "2025-01-10",
        },
        {
            "name": "Томат Бычье сердце",
            "culture": "Овощи",
            "quantity": 12,
            "expiry": "2025-12-01",
            "added": "2024-11-20",
        },
    ]
    print(render_seed_history(sample))
