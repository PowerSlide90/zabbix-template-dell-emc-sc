from dataclasses import dataclass, field


# ------------------------------------------------------------
# Common
# ------------------------------------------------------------

@dataclass(slots=True, kw_only=True)
class Tag:
    tag: str
    value: str


# ------------------------------------------------------------
# Macros
# ------------------------------------------------------------

@dataclass(slots=True, kw_only=True)
class Macro:
    macro: str
    value: str
    description: str = ""


# ------------------------------------------------------------
# Value Maps
# ------------------------------------------------------------

@dataclass(slots=True, kw_only=True)
class ValueMapEntry:
    value: str
    newvalue: str


@dataclass(slots=True, kw_only=True)
class ValueMap:
    name: str
    mappings: list[ValueMapEntry] = field(default_factory=list)


# ------------------------------------------------------------
# Items
# ------------------------------------------------------------

@dataclass(slots=True, kw_only=True)
class Item:

    # Display
    name: str
    key: str

    # Collection
    oid: str = ""

    item_type: str = "SNMP_AGENT"

    value_type: str = "UNSIGNED"

    delay: str = "1m"

    units: str = ""

    description: str = ""

    history: str = "90d"

    trends: str = "365d"

    valuemap: str | None = None

    tags: list[Tag] = field(default_factory=list)


# ------------------------------------------------------------
# Trigger
# ------------------------------------------------------------

@dataclass(slots=True, kw_only=True)
class Trigger:

    name: str

    expression: str

    priority: str = "WARNING"

    description: str = ""


# ------------------------------------------------------------
# Discovery Rule
# ------------------------------------------------------------

@dataclass(slots=True, kw_only=True)
class DiscoveryRule:

    name: str

    key: str

    oid: str

    delay: str = "1h"

    description: str = ""