from dataclasses import dataclass, field

@dataclass(slots=True)
class Macro:
    macro: str
    value: str
    description: str = ""

@dataclass(slots=True)
class ValueMapEntry:
    value: str
    newvalue: str

@dataclass(slots=True)
class ValueMap:
    name: str
    mappings: list[ValueMapEntry] = field(default_factory=list)

@dataclass(slots=True)
class Item:
    name: str
    key: str
    oid: str
    value_type: str = "UNSIGNED"
    delay: str = "1m"
    units: str = ""