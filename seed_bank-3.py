# === Stage 3: Хранилище в памяти ===
# Project: SeedBank
import datetime

class Seed:
    def __init__(self, name, culture, quantity, shelf_life):
        self.id = None
        self.name = name
        self.culture = culture
        self.quantity = quantity
        self.shelf_life = shelf_life
        self.created_at = datetime.datetime.now()

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_culture(self):
        return self.culture

    def set_culture(self, value):
        self.culture = value

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, value):
        self.quantity = value

    def get_shelf_life(self):
        return self.shelf_life

    def set_shelf_life(self, value):
        self.shelf_life = value

    def __repr__(self):
        return f"Seed(id={self.id}, name={self.name}, culture={self.culture}, quantity={self.quantity}, shelf_life={self.shelf_life})"


class SeedStorage:
    def __init__(self):
        self._seeds = {}
        self._counter = 0

    def add_seed(self, seed):
        self._counter += 1
        seed.set_id(self._counter)
        self._seeds[self._counter] = seed
        return seed

    def get_seed(self, seed_id):
        return self._seeds.get(seed_id)

    def get_all_seeds(self):
        return list(self._seeds.values())

    def __len__(self):
        return len(self._seeds)

    def __repr__(self):
        return f"SeedStorage(count={len(self._seeds)}, seeds={self._seeds})"


if __name__ == "__main__":
    storage = SeedStorage()

    tomato = Seed("Томат", "Овощные", 150, datetime.timedelta(days=180))
    bean = Seed("Фасоль", "Овощные", 80, datetime.timedelta(days=210))
    pea = Seed("Горох", "Овощные", 120, datetime.timedelta(days=150))

    storage.add_seed(tomato)
    storage.add_seed(bean)
    storage.add_seed(pea)

    print(f"Всего сортов: {len(storage)}")
    print(f"Первый сорт: {storage.get_seed(1)}")
    print(f"Сорт по id 2: {storage.get_seed(2)}")
    print("Все сорта:")
    for seed in storage.get_all_seeds():
        print(seed)
