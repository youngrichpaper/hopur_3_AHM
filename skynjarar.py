#skynjarar

import smbus
import motor as m
import time

i2c_bus = smbus.SMBus(1)
i2c_address1 = 0x71
i2c_address2 = 0x70


def searching(): #Leitar af hindrun

    i2c_bus.write_byte_data(i2c_address1, 0, 0x51)  # Tell sensor to scan in mm
    high1 = i2c_bus.read_byte_data(i2c_address1, 2)  # Read the high byte of the value
    #print(high) # print the value of High byte
    
    low1 = i2c_bus.read_byte_data(i2c_address1, 3)  # Read the low byte of the value
    #print(low) # print the value of low byte
    current_value1 = high1 * 256 + low1
    i2c_bus.write_byte_data(i2c_address2, 0, 0x51)

    high2 = i2c_bus.read_byte_data(i2c_address2, 2)
    
    low2 = i2c_bus.read_byte_data(i2c_address2, 3)

    
    current_value2 = high2 * 256 + low2 

    print(current_value1,current_value2)

    
    if 0 < current_value1 <= 40:
        hindrun_vinstri = 1
    else:
        hindrun_vinstri = 0
    
    if 0 < current_value2 <= 40:
        hindrun_haegri = 1
    else:
        hindrun_haegri = 0
    
    time.sleep(0.1)  # Sleep for some

    return hindrun_vinstri, hindrun_haegri


def skynja():
    while True:
        hindrun_vinstri, hindrun_haegri = searching()
        if hindrun_vinstri == 1:
            m.stop()
            m.rotate_by_CW(60)
            time.sleep(1)
        elif hindrun_haegri == 1:
            m.stop()
            m.rotate_by_CCW(60)
            time.sleep(1)
        else:
            m.forwards(150)
