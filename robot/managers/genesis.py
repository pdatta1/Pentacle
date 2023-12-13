

from typing import * 
from robot.interfaces.base import RobotAbilitytManagerBase, RobotAbilityBase
from robot.dataclasses.manager import ManagerInfo
from robot.dataclasses.ability import RobotAbilityInfo

class Genesis(RobotAbilitytManagerBase): 

    def __init__(
        self,
        manager_name: str,
        manager_desc: str 
    ) -> None:
        self.abilities: List[RobotAbilityBase] = [] 
        self.manager_info = ManagerInfo(manager_name=manager_name, manager_desc=manager_desc)

    def add_ability(self, ability: RobotAbilityBase) -> None:
        if ability.ability_info.id in self.abilities: 
            raise Exception(f'Ability [{ability.ability_info.id}] Already Enagaged')
        self.abilities.append(ability)

    def remove_ability(self, ability: RobotAbilityBase) -> None:
        if ability.ability_info.id not in self.abilities: 
            raise Exception(f'Ability [{ability.ability_info.id}] is not Registered')
        self.abilities.remove(ability)

    def run_abilities(self) -> None:
        for ability in self.abilities:
            ability.execute() 

    def __repr__(self) -> str:
        if self.manager_info is not None:
            return repr(self.manager_info)
        return 'Manager Info is not Available'
