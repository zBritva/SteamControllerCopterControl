# -*- coding: utf-8 -*-
__author__ = 'zBritva'

import RPi.GPIO as GPIO

class PWMControl:
    throttle_pwm = None
    roll_pwm = None
    yaw_pwm = None
    pitch_pwm = None
    log = None
    append = 5

    def __init__(self, suppress_warnings=True, log=False):
        self.log = log
        # hardware PWM ports
        throttle_pin = 18
        roll_pin = 19
        yaw_pin = 12
        pitch_pin = 13

        # set GIPO mode
        GPIO.setmode(GPIO.BCM)

        # supress warnings or not
        GPIO.setwarnings(not suppress_warnings)

        # set GIPO to output
        GPIO.setup(throttle_pin, GPIO.OUT)
        GPIO.setup(roll_pin, GPIO.OUT)
        GPIO.setup(yaw_pin, GPIO.OUT)
        GPIO.setup(pitch_pin, GPIO.OUT)

        # throttle
        self.throttle_pwm = GPIO.PWM(throttle_pin, 50)
        self.throttle_pwm.ChangeFrequency(50)  # loop 20мс
        self.throttle_pwm.start(0)
        self.throttle_pwm.ChangeDutyCycle(7.5)  # neutral state of throttle

        # roll
        self.roll_pwm = GPIO.PWM(roll_pin, 50)
        self.roll_pwm.ChangeFrequency(50)  # loop 20мс
        self.roll_pwm.start(0)
        self.roll_pwm.ChangeDutyCycle(7.5)  # neutral state of roll

        # yaw
        self.yaw_pwm = GPIO.PWM(yaw_pin, 50)
        self.yaw_pwm.ChangeFrequency(50)  # loop 20мс
        self.yaw_pwm.start(0)
        self.yaw_pwm.ChangeDutyCycle(7.5)  # neutral state of yaw

        # pitch
        self.pitch_pwm = GPIO.PWM(pitch_pin, 50)
        self.pitch_pwm.ChangeFrequency(50)  # loop 20мс
        self.pitch_pwm.start(0)
        self.pitch_pwm.ChangeDutyCycle(7.5)  # neutral state of pitch

        # initiation complete

        if self.log == True:
            print 'PWMControl was init'


    def __safe__(self, percentage):
        if percentage < 0:
            percentage = 0
        if percentage > 10:
            percentage = 10
        return percentage

    def set_frequency(self, frequency):
        self.throttle_pwm.ChangeFrequency(frequency)
        self.roll_pwm.ChangeFrequency(frequency)
        self.yaw_pwm.ChangeFrequency(frequency)
        self.pitch_pwm.ChangeFrequency(frequency)

        if self.log == True:
            print 'FREQUENCY: ' + str(frequency)

    def set_throttle(self, percentage):
        if self.log == True:
            print 'throttle: ' + str(self.append + self.__safe__(percentage))

        self.throttle_pwm.ChangeDutyCycle(self.append + self.__safe__(percentage))

    def set_roll(self, percentage):
        if self.log == True:
            print 'roll: ' + str(self.append + self.__safe__(percentage))

        self.roll_pwm.ChangeDutyCycle(self.append + self.__safe__(percentage))

    def set_yaw(self, percentage):
        if self.log == True:
            print 'yaw: ' + str(self.append + self.__safe__(percentage))

        self.yaw_pwm.ChangeDutyCycle(self.append + self.__safe__(percentage))

    def set_pitch(self, percentage):
        if self.log == True:
            print 'pitch: ' + str(self.append + self.__safe__(percentage))

        self.pitch_pwm.ChangeDutyCycle(self.append + self.__safe__(percentage))

    # def set_flightmode(self, percentage):
    #     if self.log == True:
    #         print 'pitch: ' + str(self.append + self.__safe__(percentage))
    #
    #     self.throttle_pwm.ChangeDutyCycle(self.append + self.__safe__(percentage))