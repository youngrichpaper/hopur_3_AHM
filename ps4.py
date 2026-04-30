from pyPS4Controller.controller import Controller
import motor
import smbus
import time

I2C_ADDRESS = 0x50
bus = smbus.SMBus(1)
    
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press():
        motor.forwards(180)

    def on_up_arrow_release():
        motor.stop()

    def on_down_arrow_press():
        motor.backwards(180)
    
    def on_down_arrow_release():
        motor.stop()

    def on_right_arrow_press():
        motor.rotate_CW(100)
    
    def on_right_arrow_release():
        motor.stop()

    def on_left_arrow_press():
        motor.rotate_CCW(100)

    def on_left_arrow_release():
        motor.stop()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)