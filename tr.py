from gpiozero import Motor
from time import sleep

# Setup motors using gpiozero's Motor class
# Ensure the GPIO pins match how they are connected to your L298N
motorA = Motor(forward=22, backward=23, enable=17)
motorB = Motor(forward=24, backward=25, enable=27)

def control_motors():
    # Motor A forward at full speed
    motorA.forward()
    # Motor B reverse at full speed
    motorB.backward()
    sleep(5)  # run motors for 5 seconds

    # Change directions
    motorA.backward()
    motorB.forward()
    sleep(5)  # run motors for another 5 seconds

    # Stop motors
    motorA.stop()
    motorB.stop()

try:
    while True:
        control_motors()

except KeyboardInterrupt:
    # Clean up the operation
    motorA.stop()
    motorB.stop()
    print("Program terminated!")
