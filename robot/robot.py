
from robot.interfaces.base import (
    RobotBase,
    RobotStateBase,
    RobotAbilitytManagerBase
)
from robot.dataclasses.robot import RobotInfo

class Robot(RobotBase): 

    def __init__(
        self,
        state: RobotStateBase,
        manager: RobotAbilitytManagerBase,
        robot_name: str
    ) -> None:
        self.state = state 
        self.abilities_manager = manager
        self.robot_info = RobotInfo(robot_name)

    def set_state(self, state: RobotStateBase) -> None:
        self.state = state 

    def set_abilities_manager(self, manager: RobotAbilitytManagerBase) -> None:
        self.abilities_manager = manager

    def set_robot_info(self, robot_info: RobotInfo) -> None: 
        self.robot_info = robot_info

    def __repr__(self) -> str:
        if self.robot_info is not None: 
            return f'[Robot {repr(self.robot_info)}], [State: {self.state}], [Manager: {self.abilities_manager}]'
        return "No Info to Display"
    

    

