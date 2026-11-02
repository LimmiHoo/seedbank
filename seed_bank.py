# === Stage 1: Каркас модуля ===
# Project: SeedBank
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Seed:
    name: str
    culture: str
    quantity: int
    shelf_life: date
    sown: date = field(default=None)
    germination: float = field(default=None)


def make_demo_seeds() -> list[Seed]:
    today = date.today()
    return [
        Seed("Майский салат", "Салат", 200, today - __import__("datetime").timedelta(days=180)),
        Seed("Ромашка", "Цветок", 50, today - __import__("datetime").timedelta(days=365)),
        Seed("Морковь", "Овощ", 1000, today - __import__("datetime").timedelta(days=90)),
        Seed("Лук", "Овощ", 300, today - __import__("datetime").timedelta(days=120)),
        Seed("Кукуруза", "Зерно", 250, today - __import__("datetime").timedelta(days=60)),
    ]


def main() -> None:
    seeds = make_demo_seeds()
    print("SeedBank — домашний банк семян")
    print("-" * 30)
    for seed in seeds:
        years = (date.today() - seed.shelf_life).days // 365
        print(f"{seed.name} ({seed.culture})")
        print(f"  Количество: {seed.quantity}")
        print(f"  Срок годности: {seed.shelf_life}")
        print(f"  Возраст: {years} лет")
        print()


if __name__ == "__main__":
    main()
