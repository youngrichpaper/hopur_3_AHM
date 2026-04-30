from pyPS4Controller.controller import Controller
import motor
import smbus
import time

I2C_ADDRESS = 0x50
bus = smbus.SMBus(1)
    
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(speed):
        motor.forwards(speed)

    def on_up_arrow_release(speed):
        motor.stop()

    def on_down_arrow_press(speed):
        motor.backwards(speed)
    
    def on_down_arrow_release(speed):
        motor.stop()

    def on_right_arrow_press(speed):
        motor.rotate_CW(speed)
    
    def on_right_arrow_release(speed):
        motor.stop()

    def on_left_arrow_press(speed):
        motor.rotate_CCW(speed)

    def on_left_arrow_release(speed):
        motor.stop()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen()