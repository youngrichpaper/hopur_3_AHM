#skynjarar

import smbus
import motor as m
import time
import speaker as e

auto_kveikt = False

i2c_bus = smbus.SMBus(1)

i2c_address1 = 0x71 #Vinstri skynjari
i2c_address2 = 0x70 #Miðju skynjari 
i2c_address3 = 0x72 #Hægri skynjari 
i2c_bus.write_byte_data(i2c_address1, 0, 0x51)
i2c_bus.write_byte_data(i2c_address2, 0, 0x51)  # Tell sensor to scan in cm
i2c_bus.write_byte_data(i2c_address3, 0, 0x51)

def searching(): #Leitar af hindrun
    

    time.sleep(0.01)

    high1 = i2c_bus.read_byte_data(i2c_address1, 2)  # Read the high byte of the value
    #print(high) # print the value of High byte
    low1 = i2c_bus.read_byte_data(i2c_address1, 3)  # Read the low byte of the value
    #print(low) # print the value of low byte
    vinstri = high1 * 256 + low1
    time.sleep(0.08)
    high2 = i2c_bus.read_byte_data(i2c_address2, 2)
    low2 = i2c_bus.read_byte_data(i2c_address2, 3)
    midja = high2 * 256 + low2 
    time.sleep(0.08)
    high3 = i2c_bus.read_byte_data(i2c_address3, 2)
    low3 = i2c_bus.read_byte_data(i2c_address3, 3)
    haegri = high3 * 256 + low3
    time.sleep(0.08)
    # print('Vinstri:',vinstri,'Midja:',midja,'Haegri', haegri)

    
    if 0 < haegri <= 40: #Athugar fyrir hægri skynjara
        hindrun_haegri = 1
        # print(f'Hindrun HÆGRI, fjarlægð er {haegri}')
    else:
        hindrun_haegri = 0

    if 0 < midja <= 30: #Athugar fyrir miðju skynjara
        hindrun_midja = 1
        # print(f'Hindrun MIÐJA, fjarlægð er {midja}')
    else:
        hindrun_midja = 0
    
    if 0 < vinstri <= 40: #Athugar fyrir vinstri skynjara
        hindrun_vinstri = 1
        # print(f'Hindrun VINSTRI, fjarlægð er {vinstri}')
    else:
        hindrun_vinstri = 0
    
    time.sleep(0.1)  # Sleep for some

    return hindrun_vinstri, hindrun_midja, hindrun_haegri, vinstri, haegri, midja

def snuningur(att): #Fallið snýr sér þangað til skynjarar skila 0
    while True:
        hindrun_vinstri, hindrun_midja, hindrun_haegri, _, _,_ = searching()

        if hindrun_midja == 0 and hindrun_vinstri == 0 and hindrun_haegri == 0:
            m.stop()
            break

        if att == 'haegri': #Athugar hvort eigi að beygja til hægri eða vinstri
            m.rotate_CW(80)
            print(f'hægri, {hindrun_vinstri,hindrun_midja,hindrun_haegri}')
        else:
            m.rotate_CCW(80)
            print(f'vinstri, {hindrun_vinstri,hindrun_midja,hindrun_haegri}')

        time.sleep(0.01)


#Plis

def skynja(controller):
    while True:
        if controller.auto_kveikt:
            hindrun_vinstri, hindrun_midja, hindrun_haegri, vinstri, haegri, midja = searching()
            time.sleep(0.1)
            print(f'hindrun vinstri: {hindrun_vinstri} {vinstri}, hindrun miðja: {hindrun_midja} {midja}, hindrun hægri: {hindrun_haegri} {haegri}')
            #Fer yfir skynjara og athugar hvort þeir skynja hindrun.
            if hindrun_midja == 1:
                m.stop()
                time.sleep(0.01)
                # e.not_important()
                if vinstri <= haegri:
                    snuningur('haegri')
                else:
                    snuningur('vinstri')

                time.sleep(0.1)
            elif hindrun_vinstri == 1:
                m.stop()
                time.sleep(0.01)
                # e.not_important()
                snuningur('haegri')
                time.sleep(0.1)
            elif hindrun_haegri == 1:
                m.stop()
                time.sleep(0.01)
                e.not_important()
                snuningur('vinstri')
                time.sleep(0.1)
            else: #Fer beint áfram ef allir skynjarar skila 0.
                m.forwards(100)
                time.sleep(0.1)

        time.sleep(0.05)