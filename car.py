from gpiozero import Motor
import time
import curses

# Setup motors using gpiozero's Motor class
motorA = Motor(forward=22, backward=23, enable=17)
motorB = Motor(forward=24, backward=25, enable=27)

def forward():
    motorA.forward()
    motorB.forward()

def backward():
    motorA.backward()
    motorB.backward()

def turn_left():
    motorA.forward()
    motorB.backward()

def turn_right():
    motorA.backward()
    motorB.forward()

def stop():
    motorA.stop()
    motorB.stop()

def close_motors():
    motorA.close()
    motorB.close()

def setup_curses():
    # Set up the curses environment
    window = curses.initscr()
    curses.noecho()  # Prevent input from being echoed to the screen
    curses.cbreak()  # React to keys instantly, without requiring the Enter key to be pressed
    window.keypad(True)  # Enable special keys to be handled as special values
    return window

def main(window):
    try:
        while True:
            char = window.getch()
            if char == ord('s'):
                forward()
            elif char == ord('w'):
                backward()
            elif char == ord('d'):
                turn_left()
            elif char == ord('a'):
                turn_right()
            elif char == ord(' '):  # Spacebar
                stop()
            elif char == ord('q'):  # Quit program
                break
            time.sleep(0.1)  # Small delay to prevent high CPU usage
    except KeyboardInterrupt:
        print("Program terminated!")
    finally:
        stop()
        close_motors()  # Close motors and release GPIO pins
        curses.nocbreak()
        window.keypad(False)
        curses.echo()
        curses.endwin()

if __name__ == "__main__":
    window = setup_curses()
    main(window)

