import smbus
import time

I2C_ADDRESS = 0x50
bus = smbus.SMBus(1)

def forwards(speed):
    
    if speed > 255 or speed<0:
        print('Invalid speed')
    else:
        data = [speed, 0, speed, 1]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)

def backwards(speed):
    if speed > 255 or speed<0:
        print('Invalid speed')
    else:
        data = [speed, 1, speed, 0]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)

def rotate_CW(speed):
    if speed > 255 or speed<0:
        print('Invalid speed')
    else:
        data = [speed, 1, speed, 1]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)

def rotate_CCW(speed):
    if speed > 255 or speed<0:
        print('Invalid speed')
    else:
        data = [speed, 0, speed, 0]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)

def stop():
    data = [0, 0, 0, 0]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)