# TARS — Tactical Autonomous Robotic System

A clean baseline software project for the Raspberry Pi 5 voice-controlled robot.

## Important status
This is a reconstructed baseline, not the recovered original project and not yet verified on the physical robot. Python syntax is checked, but microphone, speaker, GPIO, motor driver, ultrasonic sensor, and Ollama integration must be tested on the actual Raspberry Pi before describing the robot as fully working.

## Features in this baseline
- Voice input using Vosk and `sounddevice`
- Spoken responses using eSpeak
- Optional local AI answers through Ollama
- Basic motor movement through `gpiozero`
- Ultrasonic distance reading through `gpiozero`
- Separate modules so each part can be tested independently

The LED matrix and music playback are intentionally not included until the exact display hardware and wiring are confirmed.

## Hardware safety
- Raspberry Pi GPIO pins are 3.3V only.
- HC-SR04 ECHO is typically 5V. Use a voltage divider or level shifter before connecting it to a Pi GPIO pin.
- Use a suitable external motor supply and common ground between Pi and motor driver.
- Keep wheels lifted during initial motor tests and have a physical power cutoff available.
- Do not power motors from the Raspberry Pi 5V pin.

## Project structure
```text
TARS_Clean_Baseline/
├── main.py
├── config.py
├── requirements.txt
├── tars/
│   ├── __init__.py
│   ├── voice_input.py
│   ├── voice_output.py
│   ├── ai_brain.py
│   ├── motors.py
│   └── distance_sensor.py
├── tests/
│   ├── test_ai.py
│   ├── test_voice_output.py
│   ├── test_motors.py
│   └── test_distance.py
└── docs/
    └── hardware_and_setup.md
```

## Setup on Raspberry Pi OS
1. Install Python 3 and create a virtual environment:
   ```bash
   sudo apt update
   sudo apt install -y python3-venv python3-pip espeak-ng
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Install and start Ollama separately if you want local AI responses. Pull a model that your Pi can run, then set `OLLAMA_MODEL` in `config.py` to the exact installed model tag.
4. Download a Vosk model compatible with your language and place it in a folder named `model` in the project root. Set `VOSK_MODEL_PATH` if you use another path.
5. Review every GPIO pin in `config.py` and compare it with your actual wiring.
6. Run individual checks from the project root:
   ```bash
   python tests/test_ai.py
   python tests/test_voice_output.py
   python tests/test_distance.py
   python tests/test_motors.py
   ```
   Run motor tests only after checking the wiring and lifting the wheels.
7. Start TARS:
   ```bash
   python main.py
   ```

## Voice commands
The baseline recognises simple phrases such as:
- `hey tars`
- `forward`
- `backward`
- `left`
- `right`
- `stop`
- `what is ...` (sent to the local AI service)

Speech recognition accuracy depends on microphone selection, room noise, and the Vosk model.

## Configuration
Edit `config.py` before running. In particular, check the audio device index, GPIO pins, motor speed, sensor pins, Vosk model path, and Ollama model tag.

## Project status checklist
- [x] Source files created
- [x] Python syntax compilation check
- [ ] Install dependencies on Raspberry Pi
- [ ] Confirm audio input device and Vosk model
- [ ] Confirm Ollama endpoint and model
- [ ] Verify GPIO pin mapping against actual wiring
- [ ] Test ultrasonic sensor safely
- [ ] Test each motor with wheels lifted
- [ ] Run full voice-to-action test on the robot
