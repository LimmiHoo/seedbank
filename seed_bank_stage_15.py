# === Stage 15: Прогноз сроков ===
# Project: SeedBank
from datetime import date, timedelta


class Prognosis:
    def __init__(self, name, culture, quantity, shelf_life):
        self.name = name
        self.culture = culture
        self.quantity = quantity
        self.shelf_life = shelf_life

    def get_intervals(self):
        return [self.shelf_life]

    def get_next_intervals(self):
        return self.get_intervals()

    def get_next_date(self, current_date):
        return current_date + timedelta(days=self.shelf_life)

    def get_next_dates(self, current_date):
        return [self.get_next_date(current_date)]
