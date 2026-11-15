# === Stage 7: Теги ===
# Project: SeedBank
import json
from datetime import date


class Tag:
    def __init__(self, name):
        self.name = name


class VarietyTags:
    def __init__(self, tags=None):
        self._tags = list(tags) if tags else []

    def add(self, name):
        if not name:
            return False
        if name in self._tags:
            return False
        self._tags.append(name)
        return True

    def remove(self, name):
        return self._tags.remove(name) if name in self._tags else False

    def has(self, name):
        return name in self._tags

    def search(self, query):
        return [tag for tag in self._tags if query.lower() in tag.lower()]

    def names(self):
        return list(self._tags)

    def to_dict(self):
        return self.names()

    @classmethod
    def from_dict(cls, data):
        if not data:
            return cls()
        return cls(data)


class Variety:
    def __init__(self, name, culture, quantity, shelf_life, tags=None):
        self.name = name
        self.culture = culture
        self.quantity = quantity
        self.shelf_life = shelf_life
        self.tags = VarietyTags(tags)

    def add_tag(self, name):
        return self.tags.add(name)

    def remove_tag(self, name):
        return self.tags.remove(name)

    def search_tags(self, query):
        return self.tags.search(query)

    def to_dict(self):
        return {
            "name": self.name,
            "culture": self.culture,
            "quantity": self.quantity,
            "shelf_life": self.shelf_life,
            "tags": self.tags.to_dict(),
        }

    @classmethod
    def from_dict(cls, data):
        if not data:
            return None
        return cls(
            data["name"],
            data["culture"],
            data["quantity"],
            data["shelf_life"],
            data.get("tags"),
        )


if __name__ == "__main__":
    sample = {
        "name": "Розмарин",
        "culture": "Растение",
        "quantity": 100,
        "shelf_life": "2026-01-01",
        "tags": ["аромат", "декор", "med"],
    }
    variety = Variety.from_dict(sample)
    print(variety.name, variety.tags.names())
    print(variety.search_tags("de"))
    print(variety.add_tag("мощность"))
    print(variety.search_tags("мощ"))
    print(variety.remove_tag("декор"))
    print(variety.search_tags("дек"))
    print(variety.tags.to_dict())
