from robot.interfaces.base import RobotStateBase
from robot.dataclasses.robot import RobotStateInfo

class Awake(RobotStateBase): 

    def __init__(
        self,
        state_name, 
        state_desc
    ) -> None:
        self.state_info = RobotStateInfo(state_name=state_name, state_desc=state_desc)
        
        
    def execute(self) -> None:
        pass 

    def __repr__(self) -> str:
        if self.state_info is not None: 
            return repr(self.state_info)
        return 'State Info is not Available'

    