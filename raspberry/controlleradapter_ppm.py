# -*- coding: utf-8 -*-
__author__ = 'zBritva'

from RPIO import PWM
import array

class PPMControl:
    gpio = 18 #Default
    control_ppm = None
    period = 20000  # Default 20ms
    channel_count = 6  # default channel count 6
    default_channel_width = period / 10
    default_channel_value = 150

    channel_values = array.array()

    def __init__(self, gpio=18, period=20000, ch_count=6):
        self.gpio = gpio
        self.period = period
        self.channel_count = ch_count
        self.control_ppm = PWM.Servo()

        PWM.setup()

        # add channels and set init value as 150
        for ch in range(1,self.channel_count):
            PWM.init_channel(ch,self.period)
            PWM.add_channel_pulse(ch, self.gpio, self.default_channel_width, self.default_channel_value)
            self.default_channel_value.insert(ch, self.default_channel_value)
