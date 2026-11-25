# Hardware and setup notes

## GPIO numbering
The baseline uses BCM numbering:
- Left motor forward: GPIO 5
- Left motor backward: GPIO 6
- Right motor forward: GPIO 13
- Right motor backward: GPIO 19
- Ultrasonic trigger: GPIO 23
- Ultrasonic echo: GPIO 24

These values are carried forward from the previously discussed wiring, but MUST be checked against the robot before powering anything.

## Motor driver
- Use a separate, suitable motor battery/supply.
- Connect the motor driver's ground and Raspberry Pi ground together.
- Check the driver enable pins/jumpers (for example ENA and ENB on an L298N).
- Never connect motor supply voltage to a GPIO pin.
- Lift wheels for initial tests.

## HC-SR04 ultrasonic sensor
- VCC to suitable 5V supply and GND to common ground.
- TRIG to GPIO 23.
- ECHO to GPIO 24 only through a suitable voltage divider/level shifter because the ECHO signal is typically 5V.
- Confirm the exact sensor model before wiring.

## Audio
Check available input devices on the Pi:
```bash
python -c "import sounddevice as sd; print(sd.query_devices())"
```
Set `AUDIO_DEVICE` in `config.py` only after identifying the correct microphone.

## Ollama
Check that Ollama is running and that the model tag in `config.py` matches an installed model. The model must be one the Raspberry Pi can run within its memory and performance limits.
