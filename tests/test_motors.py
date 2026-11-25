from tars.motors import RobotMotors
from time import sleep

if __name__ == "__main__":
    print("SAFETY: Lift the robot so its wheels cannot touch the ground.")
    input("Press Enter only after checking wiring and motor power...")
    motors = RobotMotors()
    try:
        print("Testing forward briefly.")
        motors.forward(0.3)
        sleep(1)
        print("Testing backward briefly.")
        motors.backward(0.3)
    finally:
        motors.close()
