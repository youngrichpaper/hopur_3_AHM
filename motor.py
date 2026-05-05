import smbus
import time

I2C_ADDRESS = 0x50
bus = smbus.SMBus(1)

def forwards(speed, curve = 0, direction = 0):
    if direction == 0:
        if speed > 255 or speed<0:
            print('Invalid speed')
        else:
            data = [speed  , 0, int(speed*0.9), 1]
    elif direction == 1:
        data = [speed, 0, int(speed*curve),1]
    elif direction == 2:
        data = [int(speed*curve), 0, speed, 1]
    
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)
    time.sleep(0.01)

def backwards(speed, curve = 0, direction = 0):
    if direction == 0:
        if speed > 255 or speed<0:
            print('Invalid speed')
        else:
            data = [speed  , 1, int(speed*0.9), 0]
    elif direction == 1:
        data = [speed, 1, int(speed*curve),0]
    elif direction == 2:
        data = [int(speed*curve), 1, speed, 0]

    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)
    time.sleep(0.01)

def stop():
    data = [0, 0, 0, 0]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)
    time.sleep(0.01)

def rotate_CW(speed):
    if speed > 255 or speed<0:
        print('Invalid speed')
    else:
        data = [speed, 0, int(speed*0.86), 0]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)
    time.sleep(0.01)
def rotate_CCW(speed):
    if speed > 255 or speed<0:
        print('Invalid speed')
    else:
        data = [speed, 1, int(speed*0.86), 1]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)
    time.sleep(0.01)
    
def rotate_by_CW(theta, v=100):
    pi = 3.141592
    x = 0.123
    k = pi * 1/(360*x)
    l = 17.21
    t = k*theta*l/v
    rotate_CW(v)
    time.sleep(t)
    stop()

def rotate_by_CCW(theta, v=100):
    pi = 3.141592
    k = 25*pi/1251
    l = 17.21
    t = k*theta*l/v
    rotate_CCW(v)
    time.sleep(t)
    stop()

def turn(speed, curve, right):
    speed1 = speed
    speed2 = int(speed*curve/100)
    if right == True:
        data = [speed1, 0, speed2, 1]
    else: 
        data = [speed2, 0, speed1, 1]


def drive(y_speed, x_speed):
    curve = 1 - abs(x_speed)/250
    if x_speed<0: turn = 2
    elif x_speed>0: turn = 1
    else: turn = 0
    if y_speed>0:
        forwards(y_speed, curve, turn)
        print(f'Áfram {y_speed}, beygja {curve}, í {turn}')
    elif y_speed<0:
        backwards(abs(y_speed), curve, turn)
        print(f'Áfram {y_speed}, beygja {curve}, í {turn}')
    

def dance():
    for i in range(1,11):
        speed = i*20
        forwards(speed)
        time.sleep(0.5)
    stop()
    time.sleep(1)

    for i in range(1,11):
        speed = i*20
        backwards(speed)
        time.sleep(0.5)
    stop()
    time.sleep(1)

    for i in range(1,11):
        speed = i*20
        rotate_CW(speed)
        time.sleep(1)
    stop()
    time.sleep(1)

    for i in range(1,11):
        speed = i*20
        rotate_CCW(speed)
        time.sleep(1)
    stop()
    time.sleep(1)
