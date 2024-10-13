import RPi.GPIO as GPIO
import time
#import sys
import threading

# GPIO pin definitions for Motor 1
EN_A = 12  # GPIO12 (PWM)
IN1_A = 5
IN2_A = 6

# GPIO pin definitions for Motor 2
EN_B = 18  # GPIO18 (PWM)
IN1_B = 16
IN2_B = 20

# GPIO pin definitions for Motor 3
EN_C = 13  # GPIO (PWM)
IN1_C = 21
IN2_C = 26

# GPIO pin definitions for Motor 4
EN_D = 19  # GPIO (PWM)
IN1_D = 23
IN2_D = 24

# Maximum duty cycle
MAX_DUTY_CYCLE = 100

# Initialize GPIO
GPIO.setmode(GPIO.BCM)

# Setup Motor 1 pins
GPIO.setup(EN_A, GPIO.OUT)
GPIO.setup(IN1_A, GPIO.OUT)
GPIO.setup(IN2_A, GPIO.OUT)

# Setup Motor 2 pins
GPIO.setup(EN_B, GPIO.OUT)
GPIO.setup(IN1_B, GPIO.OUT)
GPIO.setup(IN2_B, GPIO.OUT)

# Setup Motor 3 pins
GPIO.setup(EN_C, GPIO.OUT)
GPIO.setup(IN1_C, GPIO.OUT)
GPIO.setup(IN2_C, GPIO.OUT)

# Setup Motor 4 pins
GPIO.setup(EN_D, GPIO.OUT)
GPIO.setup(IN1_D, GPIO.OUT)
GPIO.setup(IN2_D, GPIO.OUT)

# Initialize PWM
pwm_A = GPIO.PWM(EN_A, 1000)
pwm_B = GPIO.PWM(EN_B, 1000)
pwm_C = GPIO.PWM(EN_B, 1000)
pwm_D = GPIO.PWM(EN_B, 1000)

pwm_A.start(0)
pwm_B.start(0)
pwm_C.start(0)
pwm_D.start(0)

def set_motor_direction(motor, direction):
    if motor == 1:
        IN1 = IN1_A
        IN2 = IN2_A
    elif motor == 2:
        IN1 = IN1_B
        IN2 = IN2_B
    elif motor == 3:
        IN1 = IN1_C
        IN2 = IN2_C
    elif motor == 4:
        IN1 = IN1_D
        IN2 = IN2_D
    else:
        print("Invalid motor number")
        return
    if direction == 'forward':
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
    elif direction == 'backward':
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
    else:
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
    print(f"Motor {motor} direction set to {direction}")

def set_motor_speed(motor, speed):
    speed = min(max(speed, 0), MAX_DUTY_CYCLE)
    if motor == 1:
        pwm_A.ChangeDutyCycle(speed)
    elif motor == 2:
        pwm_B.ChangeDutyCycle(speed)
    elif motor == 3:
        pwm_C.ChangeDutyCycle(speed)
    elif motor == 4:
        pwm_D.ChangeDutyCycle(speed)
    else:
        print("Invalid motor number")
    print(f"Motor {motor} speed set to {speed}% duty cycle")

def accelerate_motor(motor, start_speed, end_speed, step_delay=0.02):
    # Accelerate or decelerate the motor from start_speed to end_speed.
    start_speed = max(min(start_speed, MAX_DUTY_CYCLE), 0)
    end_speed = max(min(end_speed, MAX_DUTY_CYCLE), 0)
    if start_speed < end_speed:
        # Accelerate
        for speed in range(int(start_speed), int(end_speed) + 1):
            set_motor_speed(motor, speed)
            time.sleep(step_delay)
    else:
        # Decelerate
        for speed in range(int(start_speed), int(end_speed) -1, -1):
            set_motor_speed(motor, speed)
            time.sleep(step_delay)
    print(f"Motor {motor} reached speed {end_speed}%")

def motor_control_thread(motor, direction, start_speed, end_speed, step_delay=0.099, run_time=1):
    # Thread function to control a motor
    set_motor_direction(motor, direction)
    accelerate_motor(motor, start_speed, end_speed, step_delay)
    # Run the motor at end_speed for specified run_time
    time.sleep(run_time)
    # Decelerate the motor back to start_speed
    accelerate_motor(motor, end_speed, start_speed, step_delay)
    # Stop the motor
    set_motor_direction(motor, 'stop')
    set_motor_speed(motor, 0)
    print(f"Motor {motor} stopped")

try:
    # Define thread for Motor 1
    motor1_thread = threading.Thread(target=motor_control_thread, args=(1, 'backward', 10, MAX_DUTY_CYCLE))

    # Define thread for Motor 2
    motor2_thread = threading.Thread(target=motor_control_thread, args=(2, 'backward', 10, MAX_DUTY_CYCLE))

    # Define thread for Motor 3
    motor3_thread = threading.Thread(target=motor_control_thread, args=(3, 'backward', 10, MAX_DUTY_CYCLE))

    # Define thread for Motor 4
    motor4_thread = threading.Thread(target=motor_control_thread, args=(4, 'backward', 10, MAX_DUTY_CYCLE))

    # Start both threads
    motor1_thread.start()
    motor2_thread.start()
    motor3_thread.start()
    motor4_thread.start()

    # Wait for both threads to complete
    motor1_thread.join()
    motor2_thread.join()
    motor3_thread.join()
    motor4_thread.join()

finally:
    pwm_A.stop()
    pwm_B.stop()
    pwm_C.stop()
    pwm_D.stop()
    GPIO.cleanup()
