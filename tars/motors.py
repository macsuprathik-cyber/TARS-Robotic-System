from gpiozero import Motor
from time import sleep
import config


class RobotMotors:
    def __init__(self):
        self.left = Motor(
            forward=config.MOTOR_LEFT_FORWARD,
            backward=config.MOTOR_LEFT_BACKWARD,
        )
        self.right = Motor(
            forward=config.MOTOR_RIGHT_FORWARD,
            backward=config.MOTOR_RIGHT_BACKWARD,
        )

    def stop(self):
        self.left.stop()
        self.right.stop()

    def forward(self, seconds=config.MOVE_SECONDS):
        self.left.forward(config.MOTOR_SPEED)
        self.right.forward(config.MOTOR_SPEED)
        sleep(seconds)
        self.stop()

    def backward(self, seconds=config.MOVE_SECONDS):
        self.left.backward(config.MOTOR_SPEED)
        self.right.backward(config.MOTOR_SPEED)
        sleep(seconds)
        self.stop()

    def left_turn(self, seconds=config.MOVE_SECONDS):
        self.left.backward(config.MOTOR_SPEED)
        self.right.forward(config.MOTOR_SPEED)
        sleep(seconds)
        self.stop()

    def right_turn(self, seconds=config.MOVE_SECONDS):
        self.left.forward(config.MOTOR_SPEED)
        self.right.backward(config.MOTOR_SPEED)
        sleep(seconds)
        self.stop()

    # Short aliases used by main.py
    def left(self, seconds=config.MOVE_SECONDS):
        self.left_turn(seconds)

    def right(self, seconds=config.MOVE_SECONDS):
        self.right_turn(seconds)

    def close(self):
        self.stop()
        self.left.close()
        self.right.close()
