from pyPS4Controller.controller import Controller
import threading
import motor
import numpy
import time
import skynjarar as s


y_speed = 0
x_speed = 0
turning = False
driving= False



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
        self.y_speed = 0
        self.x_speed= 0
        self.turning = False
        self.driving = False
        self.going_forward = False
        self.going_backwards = False
        

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

    def on_x_press(self):
        
        s.auto_kveikt = not s.auto_kveikt

        if s.auto_kveikt:
            motor.stop()
            print("AUTO KVEIKT")
        else:
            motor.stop()
            print("AUTO SLÖKKT")

    
    def on_circle_release(self):
        s.auto_kveikt = False
        motor.stop()
        print("STOPP")

    
    def on_L3_left(self, value):
        if value< -2000:
            self.x_speed = -int(numpy.interp(abs(value), [8000, 32767], [0,255]))
            self.turning = True

        elif value> -2000 and self.turning:
            self.x_speed = 0
            self.turning = False

    def on_L3_right(self, value):
        if value> 2000:
            x_speed = int(numpy.interp(abs(value), [8000, 32767], [0,255]))

        elif value< 2000 and self.turning:
            self.x_speed = 0
            self.turning = False

    def on_R2_press(self, value):
        if value > -25000 and not(going_backwards):
            y_speed = int(numpy.interp(value, [-25000, 32767], [0,255]))
            going_forward = True

    def on_R2_release(self):
        if self.going_forward:
            self.y_speed = 0
            self.going_forward = False

    def on_L2_press(self, value):
        if value > -25000 and not(self.going_forward):
            self.y_speed = -int(numpy.interp(value, [-25000, 32767], [0,255]))
            self.going_backwards = True
    
    def on_L2_release(self):
        if self.going_backwards:
            self.y_speed = 0
            self.going_backwards = False

# controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# # you can start listening before controller is paired, as long as you pair it within the timeout window
# controll = threading.Thread(target=keyrsla, daemon=True)
# # controller.listen(timeout=60)
# controll.start()

# while True:
#     motor.drive(y_speed, x_speed)
#     print(f'Hraði: {y_speed}, Áfram? {going_forward}, Afturábak? {going_backwards}')