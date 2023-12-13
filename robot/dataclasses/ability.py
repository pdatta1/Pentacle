
import uuid
from dataclasses import dataclass, field

@dataclass(frozen=True)
class RobotAbilityInfo: 
    ability_desc: str 
    ability_parent: str 
    id: str = field(init=False, default_factory=lambda: str(uuid.uuid4()))
