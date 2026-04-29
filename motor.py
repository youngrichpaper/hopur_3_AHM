import smbus
import time

I2C_ADDRESS = 0x50
bus = smbus.SMBus(1)

def forward(speed):
    
    if speed > 255 or speed<0:
        print('Invalid speed')
    else:
        data = [speed, 1, speed, 0]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)

def stop():
    data = [0, 0, 0, 0]
    bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)