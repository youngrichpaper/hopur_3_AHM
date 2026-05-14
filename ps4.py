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
        self.turning = False
        self.driving = False
        self.going_forward = False
        self.going_backwards = False
        self.auto_speed = 100
        self.pressed = False
        self.camera_queue = camera_queue

        # Servo stillingar
        self.servo_angle = 90
        v.rotate_s1(self.servo_angle)

        self.servo_direction = 0
        self.servo_step = 2
        self.servo_delay = 0.03

        self.servo_thread = threading.Thread(target=self.servo_loop, daemon=True)
        self.servo_thread.start()
        

    def on_up_arrow_press(self):
        if s.auto_kveikt:
            while self.pressed and self.auto_speed <=255:
                self.auto_speed += 1
                time.sleep(0.5)
    def on_down_arrow_press(self):
        if s.auto_kveikt:
            while self.pressed and self.auto_speed >=1:
                self.auto_speed -= 1
                time.sleep(0.5)
        
    def on_up_down_arrow_release(self):
        if s.auto_kveikt:
            self.pressed = False
            
    def on_circle_press(self):
        s.auto_kveikt = False
        self.x_speed = 0
        self.y_speed = 0
        self.going_backwards = False
        self.going_forward = False
        motor.stop()
        speaker.stop()
        print('STOP!!!!!')

    def on_x_press(self):
        
        s.auto_kveikt = not s.auto_kveikt

        if s.auto_kveikt:
            motor.stop()
            print("AUTO KVEIKT")
            speaker.baby()
        else:
            motor.stop()
            print("AUTO SLÖKKT")

    def on_triangle_press(self):
        v.flag_on = not v.flag_on
    
    def on_square_press(self):
        speaker.photo()
        self.camera_queue.put("take_picture")

    def on_L3_left(self, value):
        if not s.auto_kveikt:
            if value< -2000:
                self.x_speed = -int(numpy.interp(abs(value), [8000, 32767], [0,255]))
                self.turning = True

            elif value> -2000:
                self.x_speed = 0
                self.turning = False
    def on_L3_right(self, value):
        if not s.auto_kveikt:
            if value> 2000:
                self.x_speed = int(numpy.interp(abs(value), [8000, 32767], [0,255]))

            elif value< 2000:
                self.x_speed = 0
                self.turning = False

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
            self.servo_direction = -1
        else:
            self.servo_direction = 0

    def on_R3_right(self, value): #Færa servo1 til hægri
        if value > 2000:
            self.servo_direction = 1
        else:
            self.servo_direction = 0

    def on_R2_press(self, value):
        if not s.auto_kveikt:

            if value > -25000 and not(self.going_backwards):
                self.y_speed = int(numpy.interp(value, [-25000, 32767], [0,255]))
                self.going_forward = True

    def on_R2_release(self):
        if not s.auto_kveikt:
            self.y_speed = 0
            self.going_forward = False

    def on_L2_press(self, value):
        if not s.auto_kveikt:
            speaker.reverse()
            if value > -25000 and not(self.going_forward):
                self.y_speed = -int(numpy.interp(value, [-25000, 32767], [0,255]))
                self.going_backwards = True
                

    
    def on_L2_release(self):
        if not s.auto_kveikt:
            self.y_speed = 0
            self.going_backwards = False
            speaker.stop()