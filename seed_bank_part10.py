# === Stage 10: Смена статуса ===
# Project: SeedBank
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from enum import Enum
from typing import Optional


class SeedStatus(Enum):
    AVAILABLE = "доступен"
    RESERVED = "забронирован"
    SOWN = "посев запланирован"
    GROWN = "выражен"
    USED = "использован"
    DISPOSED = "утилизирован"


@dataclass
class StatusTransition:
    from_status: SeedStatus
    to_status: SeedStatus
    reason: str
    date: date
