# === Stage 9: Статусы записей ===
# Project: SeedBank
from datetime import date


class SeedStatus:
    SEED = "seed"
    SOWN = "sown"
    GERMINATED = "germinated"
    HARVESTED = "harvested"
    EXPIRED = "expired"
    DISCARDED = "discarded"


STATUS_CYCLE = [
    SeedStatus.SEED,
    SeedStatus.SOWN,
    SeedStatus.GERMINATED,
    SeedStatus.HARVESTED,
    SeedStatus.EXPIRED,
    SeedStatus.DISCARDED,
]

STATUS_TRANSITIONS = {
    SeedStatus.SEED: {SeedStatus.SOWN, SeedStatus.EXPIRED, SeedStatus.DISCARDED},
    SeedStatus.SOWN: {SeedStatus.GERMINATED, SeedStatus.DISCARDED},
    SeedStatus.GERMINATED: {SeedStatus.HARVESTED, SeedStatus.DISCARDED},
    SeedStatus.HARVESTED: {SeedStatus.DISCARDED},
    SeedStatus.EXPIRED: {SeedStatus.DISCARDED},
    SeedStatus.DISCARDED: set(),
}


def is_valid_transition(from_status, to_status):
    return to_status in STATUS_TRANSITIONS.get(from_status, set())


def next_statuses(status):
    return STATUS_TRANSITIONS.get(status, set())


def earliest_lifecycle_status(statuses):
    return STATUS_CYCLE[statuses.index(min(statuses, key=STATUS_CYCLE.index))]


def latest_lifecycle_status(statuses):
    return STATUS_CYCLE[statuses.index(max(statuses, key=STATUS_CYCLE.index))]


def transition_label(from_status, to_status):
    idx = STATUS_CYCLE.index(to_status)
    return f"{from_status} -> {to_status} (шаг {idx})"
