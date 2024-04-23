# Raspberry Pi Motor Controller

This project demonstrates how to control motors using the GPIO pins on a Raspberry Pi with the help of the `gpiozero` library and the `curses` library for keyboard input. This setup allows you to control two motors to move forward, backward, turn left, and turn right based on keyboard inputs.

## Prerequisites

Before running this script, ensure you have the following:
- A Raspberry Pi with GPIO pins
- Two motors correctly connected to the Raspberry Pi GPIO pins
- Python 3 installed on your Raspberry Pi
- `gpiozero` and `curses` libraries installed. You can install them using pip:

```bash
pip install gpiozero
