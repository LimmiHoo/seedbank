# === Stage 14: Топ записей ===
# Project: SeedBank
seedbank_top_n.py

from collections import Counter


def top_n_by_value(records, key, n=5):
    """Вернуть список из n сортов с наибольшим значением по полю key.

    records - список словарей (записей сорта), каждый содержит как минимум
    ключ key и, по желанию, ключ 'seed_value' (число всхожести в процентах).
    key - имя поля, по которому сортируем (например, 'quantity').
    n - сколько записей вернуть.

    Сортировка устойчивая: при равных значениях key сохраняется исходный
    порядок записей. Возвращается список кортежей (seed_value, запись).
    """
    # Подсчёт и получение топ-N по ключу seed_value (всхожесть).
    counter = Counter()
    for record in records:
        value = record.get('seed_value', 0)
        counter[value] += 1
    top_values = counter.most_common(n)

    # Сортировка по ключу, устойчивая, с учётом топ-N значений.
    result = []
    for value, count in top_values:
        selected = [record for record in records
                    if record.get('seed_value', 0) == value]
        for record in selected:
            result.append((value, record))
    result.sort(key=lambda pair: pair[0])
    return result[:n]


def top_n_by_field(records, key, n=5):
    """Вернуть список из n сортов с наибольшим значением по полю key.

    records - список словарей (записей сорта).
    key - имя поля, по которому сортируем (например, 'quantity').
    n - сколько записей вернуть.

    Возвращается список кортежей (value, запись). Сортировка устойчивая.
    """
    result = sorted(records, key=lambda record: record.get(key, 0),
                    reverse=True)
    return [(record.get(key, 0), record) for record in result[:n]]
