from tars.distance_sensor import DistanceSensor
from time import sleep

if __name__ == "__main__":
    sensor = DistanceSensor()
    try:
        for _ in range(10):
            print("Distance:", sensor.distance_cm(), "cm")
            sleep(1)
    finally:
        sensor.close()
