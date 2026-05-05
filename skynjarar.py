#skynjarar

import smbus
import motor as m
import time
import speaker as e


i2c_bus = smbus.SMBus(1)

i2c_address1 = 0x71
i2c_address2 = 0x70
i2c_address3 = 0x72


def searching(): #Leitar af hindrun

    i2c_bus.write_byte_data(i2c_address1, 0, 0x51)
    i2c_bus.write_byte_data(i2c_address2, 0, 0x51)  # Tell sensor to scan in mm
    i2c_bus.write_byte_data(i2c_address3, 0, 0x51)

    time.sleep(0.1)

    high1 = i2c_bus.read_byte_data(i2c_address1, 2)  # Read the high byte of the value
    #print(high) # print the value of High byte
    low1 = i2c_bus.read_byte_data(i2c_address1, 3)  # Read the low byte of the value
    #print(low) # print the value of low byte
    current_value1 = high1 * 256 + low1

    high2 = i2c_bus.read_byte_data(i2c_address2, 2)
    low2 = i2c_bus.read_byte_data(i2c_address2, 3)
    current_value2 = high2 * 256 + low2 

    high3 = i2c_bus.read_byte_data(i2c_address3, 2)
    low3 = i2c_bus.read_byte_data(i2c_address3, 3)
    current_value3 = high3 * 256 + low3

    print('Vinstri:',current_value1,'Hægri:',current_value2,'Vinstri', current_value3)

    if 400 < current_value1 < 500 and 400 < current_value2 < 500:
        e.baby()
    
    if 0 < current_value3 <= 30:
        hindrun_haegri = 1
        print('Hindrun Hægri')
    else:
        hindrun_haegri = 0

    if 0 < current_value1 <= 30:
        hindrun_vinstri = 1
        print('Hindrun Miðja')
    else:
        hindrun_vinstri = 0
    
    if 0 < current_value2 <= 30:
        hindrun_midja = 1
        print('Hindrun vinstri')
    else:
        hindrun_midja = 0
    
    time.sleep(0.1)  # Sleep for some

    return hindrun_vinstri, hindrun_midja, hindrun_haegri, current_value1, current_value3


def skynja():
    while True:
        hindrun_vinstri, hindrun_midja, hindrun_haegri, vinstri, haegri = searching()
        time.sleep(0.1)
        while hindrun_midja == 1:
            m.stop()
            time.sleep(0.01)
            e.not_important()
            if vinstri <= haegri:
                m.rotate_by_CW(60)
            else:
                m.rotate_by_CCW(60)
            time.sleep(0.1)
            if hindrun_midja != 1:
                break

        # elif hindrun_vinstri == 1:
        #     m.stop()
        #     time.sleep(0.01)
        #     e.not_important()
        #     m.rotate_by_CW(60)
        #     time.sleep(0.1)
        # elif hindrun_haegri == 1:
        #     m.stop()
        #     time.sleep(0.01)
        #     e.not_important()
        #     m.rotate_by_CCW(60)
        #     time.sleep(0.1)
        # else:
        #     m.forwards(150)
        #     time.sleep(0.1)

