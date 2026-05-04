from pyPS4Controller.controller import Controller
import threading
import motor
import numpy
import time

stopped = False
going_forward = False
going_backwards = False
turning_right = False

class SilencedPyPS4Controller(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        pass

    def on_x_release(self):
        pass

    def on_triangle_press(self):
        pass

    def on_triangle_release(self):
        pass

    def on_circle_press(self):
        pass

    def on_circle_release(self):
        pass

    def on_square_press(self):
        pass

    def on_square_release(self):
        pass

    def on_L1_press(self):
        pass

    def on_L1_release(self):
        pass

    def on_L2_press(self, value):
        pass

    def on_L2_release(self):
        pass

    def on_R1_press(self):
        pass

    def on_R1_release(self):
        pass

    def on_R2_press(self, value):
        pass

    def on_R2_release(self):
        pass

    def on_up_arrow_press(self):
        pass

    def on_up_down_arrow_release(self):
        pass

    def on_down_arrow_press(self):
        pass

    def on_left_arrow_press(self):
        pass

    def on_left_right_arrow_release(self):
        pass

    def on_right_arrow_press(self):
        pass

    def on_L3_up(self, value):
        pass

    def on_L3_down(self, value):
        pass

    def on_L3_left(self, value):
        pass

    def on_L3_right(self, value):
        pass

    def on_L3_y_at_rest(self):
        pass

    def on_L3_x_at_rest(self):
        pass

    def on_L3_press(self):
        pass

    def on_L3_release(self):
        pass

    def on_R3_up(self, value):
        pass

    def on_R3_down(self, value):
        pass

    def on_R3_left(self, value):
        pass

    def on_R3_right(self, value):
        pass

    def on_R3_y_at_rest(self):
        pass

    def on_R3_x_at_rest(self):
        pass

    def on_R3_press(self):
        pass

    def on_R3_release(self):
        pass

    def on_options_press(self):
        pass

    def on_options_release(self):
        pass

    def on_share_press(self):
        pass

    def on_share_release(self):
        pass

    def on_playstation_button_press(self):
        pass

    def on_playstation_button_release(self):
        pass


class MyController(SilencedPyPS4Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
        motor.forwards(230)
        print('Út fyrir endamörk alheimsins!')

    def on_down_arrow_press(self):
        motor.backwards(230)
        print('Bakk bakk')

    def on_up_down_arrow_release(self):
        motor.stop()
        print('STOP!!!!!')

   
    def on_right_arrow_press(self):
        motor.rotate_CW(100)
        print('Hægri')

    def on_left_arrow_press(self):
        motor.rotate_CCW(100)
        print('Hitt hægri')

    def on_left_right_arrow_release(self):
        motor.stop()
        print('STOP!!!!!')
    
    def on_circle_press(self):
        motor.stop()
        print('STOP!!!!!')

    def on_L3_up(self, value):
        global stopped
        if value< -8000:
            speed = int(numpy.interp(abs(value), [8000, 32767], [1,250]))
            print(f'Áfram {speed}')
            motor.forwards(speed)
            time.sleep(0.01)
            stopped = False

        elif value> -2000 and not(stopped):
            print('Stopp')
            motor.stop()
            time.sleep(0.01)
            stopped = True
        print(value)

    def on_L3_down(self, value):
        global stopped
        if value> 8000:
            speed = int(numpy.interp(abs(value), [8000, 32767], [1,250]))
            print(f'Afturábak {speed}')
            motor.backwards(speed)
            time.sleep(0.01)
            stopped = False

        elif value< 2000 and not(stopped):
            print('Stopp')
            motor.stop()
            time.sleep(0.01)
            stopped = True
        print(value)
    # def on_R3_left(self, value):
    #     print(f'VINSTRI: {value}')

    # def on_R3_right(self, value):
    #     print(f'HÆGRI: {value}')

    def on_R3_press(self):
        print(f'ÝTA')

    def on_R3_release(self):
        print(f'SLEPPA')

def keyrsla():
    controller.listen()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controll = threading.Thread(target=keyrsla)
# controller.listen(timeout=60)
controll.start()

while True:
    print('blalbal')
    time.sleep(5)