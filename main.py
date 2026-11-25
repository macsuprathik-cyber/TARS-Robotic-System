import json
import queue
import sys
from pathlib import Path

import sounddevice as sd
from vosk import Model, KaldiRecognizer

import config
from tars.ai_brain import ask_ai
from tars.distance_sensor import DistanceSensor
from tars.motors import RobotMotors
from tars.voice_output import speak


def listen_once(model):
    audio_queue = queue.Queue()
    recognizer = KaldiRecognizer(model, config.SAMPLE_RATE)

    def callback(indata, frames, time_info, status):
        if status:
            print("Audio status:", status, file=sys.stderr)
        audio_queue.put(bytes(indata))

    print("Listening... Say a command.")
    with sd.RawInputStream(
        samplerate=config.SAMPLE_RATE,
        blocksize=8000,
        device=config.AUDIO_DEVICE,
        dtype="int16",
        channels=1,
        callback=callback,
    ):
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                return result.get("text", "").strip()


def main():
    model_path = Path(config.VOSK_MODEL_PATH)
    if not model_path.exists():
        print(f"Vosk model folder not found: {model_path}")
        print("Download a Vosk model and set VOSK_MODEL_PATH in config.py.")
        return

    model = Model(str(model_path))
    motors = RobotMotors()
    distance_sensor = DistanceSensor()

    speak("TARS is ready.")
    print("TARS is running. Press Ctrl+C to stop.")

    try:
        while True:
            text = listen_once(model)
            if not text:
                continue

            print("Heard:", text)

            if "stop" in text:
                motors.stop()
                speak("Stopped.")
            elif "forward" in text or "move ahead" in text:
                distance = distance_sensor.distance_cm()
                if distance is not None and distance < config.OBSTACLE_LIMIT_CM:
                    motors.stop()
                    speak("There is an obstacle ahead.")
                else:
                    motors.forward(config.MOVE_SECONDS)
                    speak("Moving forward.")
            elif "backward" in text or "reverse" in text:
                motors.backward(config.MOVE_SECONDS)
                speak("Moving backward.")
            elif "left" in text:
                motors.left(config.MOVE_SECONDS)
                speak("Turning left.")
            elif "right" in text:
                motors.right(config.MOVE_SECONDS)
                speak("Turning right.")
            elif "hey tars" in text or text == "hey":
                speak("Yes, I am listening.")
            else:
                answer = ask_ai(text)
                speak(answer)

    except KeyboardInterrupt:
        print("\nStopping TARS...")
    finally:
        motors.stop()
        motors.close()
        distance_sensor.close()
        speak("TARS shutting down.")


if __name__ == "__main__":
    main()
