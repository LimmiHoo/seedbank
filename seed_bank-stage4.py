# === Stage 4: Связанная сущность ===
# Project: SeedBank
from datetime import date


class SeedSowing:
    def __init__(self, seed_id, sowing_date, expected_hatch_rate=100.0):
        if not isinstance(seed_id, int):
            raise TypeError("seed_id должен быть целым числом")
        if sowing_date < date.today():
            raise ValueError("дата посева не может быть в прошлом")
        if not 0 <= expected_hatch_rate <= 100:
            raise ValueError("процент всхожести должен быть от 0 до 100")

        self.seed_id = seed_id
        self.sowing_date = sowing_date
        self.expected_hatch_rate = expected_hatch_rate
        self.planted_count = 0

    def add_planted(self, count):
        if count <= 0:
            raise ValueError("количество посеянных семян должно быть больше нуля")
        self.planted_count += count

    def get_expected_hatched(self):
        return int(self.planted_count * self.expected_hatch_rate / 100)

    def get_days_since_sowing(self):
        return (date.today() - self.sowing_date).days

    def get_sowing_info(self):
        return (
            f"Посев №{self.seed_id} от {self.sowing_date.isoformat()}: "
            f"посеяно {self.planted_count}, "
            f"ожидаемо всходов {self.get_expected_hatched()}, "
            f"прошло дней {self.get_days_since_sowing()}"
        )
