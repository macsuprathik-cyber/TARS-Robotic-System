import subprocess
import config


def speak(message: str) -> None:
    message = str(message).strip()
    if not message:
        return
    try:
        subprocess.run(
            ["espeak-ng", "-v", config.ESPEAK_VOICE, "-s", str(config.ESPEAK_SPEED), message],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except FileNotFoundError:
        print("eSpeak NG is not installed. TARS says:", message)
