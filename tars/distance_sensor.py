from gpiozero import DistanceSensor as GpioDistanceSensor
import config


class DistanceSensor:
    def __init__(self):
        self.sensor = GpioDistanceSensor(
            echo=config.ULTRASONIC_ECHO,
            trigger=config.ULTRASONIC_TRIGGER,
            max_distance=2.0,
        )

    def distance_cm(self):
        try:
            return round(self.sensor.distance * 100, 1)
        except (TimeoutError, RuntimeError):
            return None

    def close(self):
        self.sensor.close()
