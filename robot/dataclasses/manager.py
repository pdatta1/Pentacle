
import uuid 
from typing import * 
from dataclasses import dataclass, field 

from robot.dataclasses.ability import RobotAbilityInfo

@dataclass(frozen=True)
class ManagerInfo: 
    manager_name: str 
    manager_desc: str 
    abilities: List[RobotAbilityInfo] = field(default_factory=list)
    manager_id: str = field(init=False, default_factory=lambda: str(uuid.uuid4()))
