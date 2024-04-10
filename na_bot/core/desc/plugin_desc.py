from dataclasses import dataclass, field

@dataclass
class PluginDesc():
    name: str = None
    use_state = False