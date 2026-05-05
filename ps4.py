from pyPS4Controller.controller import Controller
import threading
import motor
import numpy
import time
import pygame

pygame.init()
controller1 =  pygame.joystick.Joystick(0)
controller1.init()
buttons = {'x':0, 'o':0, 't':0, 's':0,
           'L1':0, 'R1':0, 'L2':0, 'R2':0,
           'share':0, 'ps':0, 'options':0,
           'up':0, 'down':0, 'left':0, 'right':0, 'touchpad':0,
           'axis1':0., 'axis2':0., 'axis3':0., 'axis4':0.,
           'axis5':0., 'axis6':0., 'axis7':0., 'axis8':0.}
axiss = [0., 0., 0., 0., 0., 0., 0., 0.]

def getJS(name=''):

    global buttons
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            axiss[event.axis] = round(event.value,2)
        elif event.type == pygame.JOYBUTTONDOWN:
            for x, (key, val) in enumerate(buttons.items()):
                if x<10:
                    if controller1.get_button(x):buttons[key]=1
        elif event.type == pygame.JOYBUTTONUP:
            for x, (key, val) in enumerate(buttons.items()):
                if x<10:
                    if event.button == x:buttons[key]=0
    buttons['axis1'],buttons['axis2'],buttons['axis3'],buttons['axis4'],buttons['axis5'],buttons['axis6'],buttons['axis7'],buttons['axis8'] = axiss
    if name == '':
        return buttons
    else:
        return buttons[name]

def test():
    print(getJS())
    time.sleep(0.5)

stopped = False
going_forward = False
going_backwards = False
turning_right = False
turning_left = False
y_speed = 0
x_speed = 0
curve = 0
direction = 0
turning = False
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
        global stopped, going_forward, y_speed, direction
        if value< -4000:
            y_speed = int(numpy.interp(abs(value), [8000, 32767], [1,250]))
            # print(f'Áfram {y_speed}')
            # motor.forwards(y_speed, curve, direction)
            going_forward = True
            stopped = False
            direction = 1

        elif value> -2000 and not(stopped):
            y_speed = 0
            print('Stopp')
            # motor.stop()
            going_forward = False
            stopped = True
            direction = 0
        # print(value, y_speed)

    def on_L3_down(self, value):
        global stopped, going_backwards, y_speed, direction
        if value> 4000:
            y_speed = int(numpy.interp(abs(value), [8000, 32767], [0,250]))
            direction = 2
            # print(f'Afturábak {y_speed}')
            # motor.backwards(y_speed, curve, direction)
            going_backwards =True
            stopped = False

        elif value< 2000 and not(stopped):
            print('Stopp')
            direction = 0
            y_speed = 0
            # direction = 0
            going_backwards = False
            stopped = True
        # print(value, y_speed)

    def on_L3_left(self, value):
        global stopped, turning_left, going_forward, y_speed, x_speed, curve, direction, turning, turning_right
        # if going_forward:
        if value< -2000:
            x_speed = int(numpy.interp(abs(value), [8000, 32767], [0,250]))
            curve =1- (x_speed/255)
            turning_left = True
            turning = True
            turning_right = False
            # direction = 2

        elif value> -2000 and turning:
            curve = 0
            x_speed = 0
            # direction = 0
            turning_left = False
            turning = False

        # print(value, x_speed)

    def on_L3_right(self, value):
        global stopped, turning_right, going_forward, y_speed, x_speed, curve, direction, turning, turning_left
        # if going_forward:
        if value> 2000:
            x_speed = int(numpy.interp(abs(value), [8000, 32767], [1,250]))
            curve =1 - (x_speed/255)
            turning_right = True
            turning = True
            turning_left =False
            # direction = 1

        elif value< 2000 and turning:
            curve = 0
            x_speed = 0
            # direction = 0
            turning_right = False
            turning = False
        # print(value, x_speed)

    def on_R3_press(self):
        print(f'ÝTA')

    def on_R3_release(self):
        print(f'SLEPPA')

def keyrsla():
    controller.listen()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controll = threading.Thread(target=keyrsla, daemon=True)
# controller.listen(timeout=60)
controll.start()

while True:
    print(y_speed,x_speed, end='')
    if direction == 1: 
        print('Áfram', end='')
    elif direction == 2: print('Bakka', end='')
    if turning_left: print('Vinstri', end='')
    if turning_right: print('Hægri', end='')
    print('')
    time.sleep(0.1)