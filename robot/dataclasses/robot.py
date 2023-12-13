
import uuid 
from dataclasses import dataclass, field

@dataclass(frozen=True)
class RobotInfo:
    robot_name: str 
    robot_id: str = field(init=False, default_factory=lambda: str(uuid.uuid4()))


@dataclass(frozen=True)
class RobotStateInfo: 
    state_name: str 
    state_desc: str 
    state_id: str = field(init=False, default_factory=lambda: str(uuid.uuid4()))