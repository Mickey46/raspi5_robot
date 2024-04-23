from gpiozero import Motor

# Setup motors
motorA = Motor(forward=22, backward=23, enable=17)
motorB = Motor(forward=24, backward=25, enable=27)

try:
    # Your code to control motors
    pass
finally:
    motorA.close()
    motorB.close()

