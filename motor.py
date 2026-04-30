import smbus
import time

I2C_ADDRESS = 0x50
bus = smbus.SMBus(1)

def forwards(speed):
    
    if speed > 255 or speed<0:
        print('Invalid speed')
    else:
        data = [speed  , 0, int(speed*0.9), 1]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)

def backwards(speed):
    if speed > 255 or speed<0:
        print('Invalid speed')
    else:
        data = [speed, 1, int(speed*0.86), 0]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)

def stop():
    data = [0, 0, 0, 0]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)

def rotate_CW(speed):
    if speed > 255 or speed<0:
        print('Invalid speed')
    else:
        data = [speed, 1, int(speed*0.86), 1]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)

def rotate_CCW(speed):
    if speed > 255 or speed<0:
        print('Invalid speed')
    else:
        data = [speed, 0, int(speed*0.86), 0]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)

def rotate_by_CW(theta, v=150):
    pi = 3.141592
    k = 25*pi/1251
    l = 17.21
    t = k*theta*l/v
    print(f'will rotate for {t} seconds to turn {theta}° clockwise')
    rotate_CW(v)
    time.sleep(t)
    stop()

def rotate_by_CCW(theta, v=150):
    pi = 3.141592
    k = 25*pi/1251
    l = 17.21
    t = k*theta*l/v
    print(f'will rotate for {t} seconds to turn {theta}° counterclockwise')
    rotate_CCW(v)
    time.sleep(t)
    stop()


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

    