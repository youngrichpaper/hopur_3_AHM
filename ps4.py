from pyPS4Controller.controller import Controller
import threading
import motor
import numpy
import time
import skynjarar as s
import speaker
import servo as v


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

    def __init__(self,camera_queue, **kwargs):
        Controller.__init__(self, **kwargs)
        self.y_speed = 0
        self.x_speed= 0
        self.going_forward = False
        self.going_backwards = False
        self.camera_queue = camera_queue
        self.auto_kveikt = False
        self.flag_on = False
        # Servo stillingar
        self.servo_angle = 90
        v.rotate_s1(self.servo_angle)

        self.servo_direction = 0
        self.servo_step = 2
        self.servo_delay = 0.03

        # self.servo_thread = threading.Thread(target=self.servo_loop, daemon=True)
        # self.servo_thread.start()
        if self.auto_kveikt:
            self.pressed = False
            
    def on_circle_press(self):
        self.auto_kveikt = False
        self.x_speed = 0
        self.y_speed = 0
        self.going_backwards = False
        self.going_forward = False
        speaker.stop()
        print('STOP!!!!!')

    def on_x_press(self):
        self.auto_kveikt = not self.auto_kveikt
        self.x_speed = 0
        self.y_speed = 0
        if self.auto_kveikt:
            print("AUTO KVEIKT")
            speaker.baby()
        else:
            print("AUTO SLÖKKT")

    def on_triangle_press(self):
        self.flag_on = not self.flag_on
    
    def on_square_press(self):
        speaker.photo()
        self.camera_queue.put("take_picture")

    def on_L3_left(self, value):
        if not self.auto_kveikt:
            if value< -2000:
                self.x_speed = -int(numpy.interp(abs(value), [8000, 32767], [0,255]))

            elif value> -2000:
                self.x_speed = 0
    def on_L3_right(self, value):
        if not self.auto_kveikt:
            if value> 2000:
                self.x_speed = int(numpy.interp(abs(value), [8000, 32767], [0,255]))

            elif value< 2000:
                self.x_speed = 0

#Færir servo1 með R3
    def servo_loop(self): #Færir servo á meða R3 er haldið til hægri eða vinstri
        while True:
            #Breytir horni eftir stefni pinna
            if self.servo_direction != 0:
                self.servo_angle += self.servo_direction * self.servo_step

                #Held servo innan leyfilegs bils
                if self.servo_angle < 0:
                    self.servo_angle = 0

                elif self.servo_angle > 180:
                    self.servo_angle = 180

                v.rotate_s1(self.servo_angle) #Uppfæri stöðunna á servo1

            time.sleep(self.servo_delay) #Stýrir hraða á hreyfingu

    def on_R3_left(self, value): #Færa servo1 til vinstri
        if value < -2000:
            if self.servo_angle > 0:
                self.servo_angle -= 1
                v.rotate_s1(self.servo_angle)
                time.sleep(0.03)

    def on_R3_right(self, value): #Færa servo1 til hægri
        if value > 2000:
            if self.servo_angle < 180:
                self.servo_angle += 1
                v.rotate_s1(self.servo_angle)
                time.sleep(0.03)

    def on_R2_press(self, value):
        if not self.auto_kveikt:

            if value > -25000 and not(self.going_backwards):
                self.y_speed = int(numpy.interp(value, [-25000, 32767], [0,255]))
                self.going_forward = True

    def on_R2_release(self):
        if not self.auto_kveikt:
            self.y_speed = 0
            self.going_forward = False

    def on_L2_press(self, value):
        if not self.auto_kveikt:
            speaker.reverse()
            if value > -25000 and not(self.going_forward):
                self.y_speed = -int(numpy.interp(value, [-25000, 32767], [0,255]))
                self.going_backwards = True
                

    
    def on_L2_release(self):
        if not self.auto_kveikt:
            self.y_speed = 0
            self.going_backwards = False
            speaker.stop()