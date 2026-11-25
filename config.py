# Review these values against your actual Raspberry Pi wiring before running.

# Audio
AUDIO_DEVICE = None  # None uses the system default. Set an integer only after checking devices.
SAMPLE_RATE = 16000
VOSK_MODEL_PATH = "model"

# Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "phi4-mini:latest"  # Change to the exact model tag installed on your Pi.

# Motor GPIO pins (BCM numbering) — confirm against your wiring.
MOTOR_LEFT_FORWARD = 5
MOTOR_LEFT_BACKWARD = 6
MOTOR_RIGHT_FORWARD = 13
MOTOR_RIGHT_BACKWARD = 19

# Ultrasonic sensor GPIO pins (BCM numbering) — confirm wiring and level shifting.
ULTRASONIC_TRIGGER = 23
ULTRASONIC_ECHO = 24

# Motion
MOTOR_SPEED = 0.55
MOVE_SECONDS = 0.6
OBSTACLE_LIMIT_CM = 20

# Speech output
ESPEAK_VOICE = "en-us"
ESPEAK_SPEED = 145
