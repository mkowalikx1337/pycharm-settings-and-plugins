from typing import Any

MAC_EPOCH: Any
WINDOWS_EPOCH: Any
# The following two constants are defined twice in the implementation.
CALENDAR_WINDOWS_1900 = WINDOWS_EPOCH  # noqa: F821
CALENDAR_MAC_1904 = MAC_EPOCH  # noqa: F821
SECS_PER_DAY: int
ISO_FORMAT: str
ISO_REGEX: Any
ISO_DURATION: Any

def to_ISO8601(dt): ...
def from_ISO8601(formatted_string): ...
def to_excel(dt, epoch=...): ...
def from_excel(value, epoch=..., timedelta: bool = ...): ...
def time_to_days(value): ...
def timedelta_to_days(value): ...
def days_to_time(value): ...
