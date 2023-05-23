import RPi.GPIO as GPIO

class Alphabot:
    def __init__(self, ain1=12, ain2=13, bin1=20, bin2=21, ena=6, enb=26, drivingPower=50, turningPower=30):
        self.ain1 = ain1 # motor A forwards
        self.ain2 = ain2 # motor A backwards
        self.bin1 = bin1 # motor B forwards
        self.bin2 = bin2 # motor B backwards
        self.ena = ena # enable pin for motor A
        self.enb = enb # enable pin for motor B

        self.drivingPower = drivingPower # duty cycle of the PWM signal of the motors (0-100 percentage)
        self.turningPower = turningPower # duty cycle of the PWM signal of the motors  (0-100 percentage)

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.ain1, GPIO.OUT)
        GPIO.setup(self.ain2, GPIO.OUT)
        GPIO.setup(self.bin1, GPIO.OUT)
        GPIO.setup(self.bin2, GPIO.OUT)
        GPIO.setup(self.ena, GPIO.OUT)
        GPIO.setup(self.enb, GPIO.OUT)
        self.pwma = GPIO.PWM(self.ena, 500)
        self.pwmb = GPIO.PWM(self.enb, 500)
        self.pwma.start(self.drivingPower)
        self.pwmb.start(self.drivingPower)

        self.stop()

    """
    Drives forward, using both wheels
    """
    def drive_forward(self):
        self.pwma.ChangeDutyCycle(self.drivingPower)
        self.pwmb.ChangeDutyCycle(self.drivingPower)
        GPIO.output(self.ain1, GPIO.LOW)
        GPIO.output(self.ain2, GPIO.HIGH)
        GPIO.output(self.bin1, GPIO.LOW)
        GPIO.output(self.bin2, GPIO.HIGH)

    """
    Drives backwards, using both wheels
    """
    def drive_backwards(self):
        self.pwma.ChangeDutyCycle(self.drivingPower)
        self.pwmb.ChangeDutyCycle(self.drivingPower)
        GPIO.output(self.ain1, GPIO.HIGH)
        GPIO.output(self.ain2, GPIO.LOW)
        GPIO.output(self.bin1, GPIO.HIGH)
        GPIO.output(self.bin2, GPIO.LOW)

    """
    Drives while turning to the left
    """
    def drive_left(self):
        self.pwma.ChangeDutyCycle(self.turningPower)
        self.pwmb.ChangeDutyCycle(self.turningPower)
        GPIO.output(self.ain1, GPIO.HIGH)
        GPIO.output(self.ain2, GPIO.LOW)
        GPIO.output(self.bin1, GPIO.LOW)
        GPIO.output(self.bin2, GPIO.HIGH)

    """
    Drives while turning to the right
    """
    def drive_right(self):
        self.pwma.ChangeDutyCycle(self.turningPower)
        self.pwmb.ChangeDutyCycle(self.turningPower)
        GPIO.output(self.ain1, GPIO.LOW)
        GPIO.output(self.ain2, GPIO.HIGH)
        GPIO.output(self.bin1, GPIO.HIGH)
        GPIO.output(self.bin2, GPIO.LOW)

    """
    Stops both wheels and the pwm signal
    """
    def stop(self):
        self.pwma.ChangeDutyCycle(0)
        self.pwmb.ChangeDutyCycle(0)
        GPIO.output(self.ain1, GPIO.LOW)
        GPIO.output(self.ain2, GPIO.LOW)
        GPIO.output(self.bin1, GPIO.LOW)
        GPIO.output(self.bin2, GPIO.LOW)
