# === Stage 13: Серии по дням ===
# Project: SeedBank
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from itertools import groupby
from typing import Iterable, Iterator

__all__ = ["SeedSeries", "seed_series"]


@dataclass
class SeedSeries:
    """Серия подряд идущих дней с действиями над «сорт».

    Серии группируются по дате действия: все операции, совершённые за
    один день, объединяются в один элемент серии.
    """

    date: date
    actions: list[tuple[str, "SeedSeries.ActionTarget"]] = field(default_factory=list)

    @dataclass
    class ActionTarget:
        """Метка цели действия внутри серии."""

        seed_name: str
        culture: str | None = None


def seed_series(events: Iterable["SeedEvent"]) -> Iterator[SeedSeries]:
    """Сгруппировать события в серии подряд идущих дней.

    События группируются по дате. События с одной датой объединяются в
    одну серию, события разных дат образуют отдельные серии.
    """

    for _date, group in groupby(sorted(events, key=_date), key=_date):
        actions = [
            SeedSeries.ActionTarget(name, culture)
            for name, culture in [(_event.target, _event.culture) for _event in group]
        ]
        yield SeedSeries(date=_date, actions=actions)


@dataclass
class SeedEvent:
    """Сырое событие действия над «сорт» с датой и параметрами."""

    date: date
    target: str
    culture: str | None = None
    quantity: int | None = None
    germination: float | None = None
