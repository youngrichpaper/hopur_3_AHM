import smbus
import time

I2C_ADRESS = 0x50
bus = smbus.SMBus(1)

print('Hello World')