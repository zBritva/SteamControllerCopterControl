# -*- coding: utf-8 -*-
__author__ = 'zBritva'

"""Steam Controller Callback Mode example"""
import sys

from steamcontroller import SteamController, SCButtons
from steamcontroller.events import EventMapper, Pos
from steamcontroller.uinput import Keys
from raspberry.controlleradapter import PWMControl


class ControlLinker:
    pwm_control = PWMControl(True, True)
    log_mode = None
    axis_max_value = 32767
    neutral = 5.0

    def __init__(self, log_mode=False):
        self.log_mode = log_mode
        # half of 100, -50 for negative
        self.scale_factor = self.axis_max_value / self.neutral

        # if self.log_mode:
        print 'scale_factor: ' + str(self.scale_factor)

        self.pwm_control.set_frequency(50)

    def button_pressed_callback(self, evm, btn, pressed):
        if self.log_mode:
            print "Button {} was {}.".format(btn, 'pressed' if pressed else 'released')

        if btn == SCButtons.STEAM and not pressed:
            if self.log_mode:
                print "pressing the STEAM button terminates the programm"
            sys.exit()

    def touchpad_click_callback(self, evm, pad, pressed, wtf):
        if self.log_mode:
            print "Tochpad {} was {}".format(pad, 'pressed' if pressed else 'released')

    def touchpad_touch_callback(self, evm, pad, x, y):
        # if self.log_mode:
        print "Tochpad {} was touched @{},{}".format(pad, x, y)

        # left pad
        if pad == 1:
            throttle = self.neutral + y * 1.0 / self.scale_factor
            yaw = self.neutral + x * 1.0 / self.scale_factor

            # if throttle < 0:
            #     print 'CRITICAL!!!: throttle : ' + str(self.neutral) + ' + ' + str(y) + '/' + str(self.scale_factor) + ' = ' + str(throttle)

            # if yaw < 0:
            #     print 'CRITICAL!!!: yaw : ' + str(self.neutral) + ' + ' + str(x) + '/' + str(self.scale_factor) + ' = ' + str(yaw)

            self.pwm_control.set_throttle(throttle)
            self.pwm_control.set_yaw(yaw)

        # right pad
        if pad == 0:
            pitch = self.neutral + y * 1.0 / self.scale_factor
            roll = self.neutral + x * 1.0 / self.scale_factor

            # if pitch < 0:
            #     print 'CRITICAL!!!: pitch : ' + str(self.neutral) + ' + ' + str(y) + '/' + str(self.scale_factor) + ' = ' + str(pitch)

            # if roll < 0:
            #     print 'CRITICAL!!!: roll : ' + str(self.neutral) + ' + ' + str(x) + '/' + str(self.scale_factor) + ' = ' + str(roll)

            self.pwm_control.set_pitch(pitch)
            self.pwm_control.set_roll(roll)

    def stick_pressed_callback(self, evm):
        if self.log_mode:
            print "Stick pressed"

    def stick_axes_callback(self, evm, x, y):
        if self.log_mode:
            print "Stick Position is {}, {}".format(x, y)

    def evminit(self):
        evm = EventMapper()
        evm.setButtonCallback(SCButtons.STEAM, self.button_pressed_callback)
        evm.setButtonCallback(SCButtons.A, self.button_pressed_callback)
        evm.setButtonCallback(SCButtons.B, self.button_pressed_callback)
        evm.setButtonCallback(SCButtons.X, self.button_pressed_callback)
        evm.setButtonCallback(SCButtons.Y, self.button_pressed_callback)
        evm.setButtonCallback(SCButtons.LB, self.button_pressed_callback)
        evm.setButtonCallback(SCButtons.RB, self.button_pressed_callback)
        evm.setButtonCallback(SCButtons.LT, self.button_pressed_callback)
        evm.setButtonCallback(SCButtons.RT, self.button_pressed_callback)
        evm.setButtonCallback(SCButtons.LGRIP, self.button_pressed_callback)
        evm.setButtonCallback(SCButtons.RGRIP, self.button_pressed_callback)
        evm.setButtonCallback(SCButtons.START, self.button_pressed_callback)
        evm.setButtonCallback(SCButtons.BACK, self.button_pressed_callback)
        evm.setPadButtonCallback(Pos.LEFT, self.touchpad_touch_callback)
        evm.setPadButtonCallback(Pos.RIGHT, self.touchpad_click_callback, clicked=False)
        evm.setStickAxesCallback(self.stick_axes_callback)
        evm.setStickPressedCallback(self.stick_pressed_callback)
        return evm


if __name__ == '__main__':
    cl = ControlLinker()
    evm = cl.evminit()
    sc = SteamController(callback=evm.process)
    sc.run()
