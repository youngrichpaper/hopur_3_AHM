from pyPS4Controller.controller import Controller
import motor


    
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
        motor.forwards(180)

    def on_up_arrow_release(self):
        motor.stop()

    def on_down_arrow_press(self):
        motor.backwards(180)
    
    def on_down_arrow_release(self):
        motor.stop()

    def on_right_arrow_press(self):
        motor.rotate_CW(100)
    
    def on_right_arrow_release(self):
        motor.stop()

    def on_left_arrow_press(self):
        motor.rotate_CCW(100)

    def on_left_arrow_release(self):
        motor.stop()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)