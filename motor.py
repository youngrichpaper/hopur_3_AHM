import smbus
import time

I2C_ADRESS = 0x50
bus = smbus.SMbus(1)

print('Hello World')