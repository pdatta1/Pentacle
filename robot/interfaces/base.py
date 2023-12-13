
from typing import * 
from abc import ABC, abstractmethod
from robot.dataclasses.ability import RobotAbilityInfo 
from robot.dataclasses.robot import RobotInfo, RobotStateInfo
from robot.dataclasses.manager import ManagerInfo



class RobotStateBase(ABC): 
    """
        Robot State Abstract class, defines the state of the robot and 
        executes
    """
    def __init__(self) -> None:
        self.state_info: Union[RobotStateInfo, None] = None 
        
    @abstractmethod
    def execute(self) -> None: 
        pass 


class RobotAbilityBase(ABC): 
    """
        Robot Ability Abstract class, it abstract class is built as an interface
        that can be inherit to build an ability of the robot
    """
    def __init__(self) -> None:
        self.ability_info: Union[RobotInfo, None] = None 

    @abstractmethod
    def execute(self) -> None: 
        pass 


class RobotAbilitytManagerBase(ABC): 
    """
        Robot Ability Manager Base is an interface built for inheritance that
        allows a user to build an ability manager of their own design, that can later 
        be bolted onto a robot class
    """
    def __init__(self) -> None:
        self.manager_info: ManagerInfo = None 

    @abstractmethod
    def add_ability(self, ability: RobotAbilityBase) -> None: 
        pass 

    @abstractmethod
    def remove_ability(self, ability: RobotAbilityBase) -> None: 
        pass 

    @abstractmethod
    def run_abilities(self) -> None: 
        pass 



class RobotBase(ABC): 
    """
        Defines the Base of the Robot, can be inherited
        to built a custom robot class
    """

    def __init__(self) -> None:
        self.robot_info: Union[RobotAbilityInfo, None] = None 
        
    @abstractmethod
    def set_state(self, state: RobotStateBase) -> None: 
        pass 

    @abstractmethod
    def set_abilities_manager(self, manager: RobotAbilitytManagerBase) -> None: 
        pass 
