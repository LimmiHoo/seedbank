# === Stage 8: Быстрые фильтры ===
# Project: SeedBank
import datetime


def _parse_date(value):
    """Преобразует строку в дату, возвращает None при ошибке."""
    try:
        return datetime.datetime.strptime(value.strip(), "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def _today():
    return datetime.date.today()


def filter_by_date(records, predicate):
    """Применяет predicate к дате срока годности каждой записи.

    predicate должен принимать объект datetime.date и возвращать булево
    значение. Невалидные даты пропускаются.
    """
    return [record for record in records if predicate(_parse_date(record["date_expires"]))]


def filter_today(records):
    """Возвращает записи, срок годности которых истекает сегодня."""
    today = _today()
    return filter_by_date(records, lambda d: d == today)


def filter_this_week(records):
    """Возвращает записи, срок годности которых истекает на этой неделе."""
    today = _today()
    start = today - datetime.timedelta(days=today.weekday())
    end = start + datetime.timedelta(days=6)
    return filter_by_date(records, lambda d: start <= d <= end)


def filter_expired(records):
    """Возвращает записи, срок годности которых уже истёк."""
    today = _today()
    return filter_by_date(records, lambda d: d is not None and d < today)


def filter_by_date_name(records, name):
    """Возвращает записи по названию фильтра: сегодня/неделя/просроченные."""
    name = name.strip().lower()
    mapping = {
        "сегодня": filter_today,
        "на этой неделе": filter_this_week,
        "просроченные": filter_expired,
    }
    return mapping.get(name, filter_by_date_name)(records)
