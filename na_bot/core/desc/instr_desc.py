from dataclasses import dataclass
from enum import Enum, auto

class InstrMode(Enum):
    STANDARD = auto()
    ADVICE = auto()
    FALLBACK = auto()

@dataclass
class InstrDesc():
    name: str = None
    bypass: bool = False
    mode: InstrMode = InstrMode.STANDARD
    always_save_state: bool = False
