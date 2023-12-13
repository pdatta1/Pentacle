
import os 
import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from robot.robot import Robot
from robot.managers.genesis import Genesis
from robot.states.awake import Awake
from robot.dataclasses.robot import RobotInfo


def test_robot() -> None: 

    robot_state = Awake('awake', 'when robot is alive')
    robot_manager = Genesis('Genesis', '1st Legacy Manager')
    robot = Robot(robot_state, robot_manager, 'Penacle')
    
    print('Robot: ', robot)


if __name__ == '__main__': 
    test_robot() 