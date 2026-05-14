# Pakkar teknir inn
import smbus
import time

# Adressan á mótorunum
I2C_ADDRESS = 0x50
bus = smbus.SMBus(1)

# ÁFRAM
def forwards(speed, curve = 0, direction = 0):
    # Fallið tekur inn hraða og beygju og átt

    if direction == 0: # Ef áttin er 0 fer hann beint áfram
        data = [speed  , 0, speed, 1]
    elif direction == 1: # Ef áttin er 1 er beygt til vinstri
        data = [speed, 0, int(speed*curve),1]
    elif direction == 2: # Ef áttin er 2 er beygt til hægri
        data = [int(speed*curve), 0, speed, 1]
    try:
        # Gögn send á mótora
        bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)
    except OSError:
        pass
    time.sleep(0.01)

# AFTURÁBAK
def backwards(speed, curve = 0, direction = 0):
    # Fallið virkar alveg eins og áfram nema farið er aftuábak en ekki áfram
    if direction == 0:
        data = [speed  , 1, speed, 0]
    elif direction == 1:
        data = [speed, 1, int(speed*curve),0]
    elif direction == 2:
        data = [int(speed*curve), 1, speed, 0]

    try:
        bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)
    except OSError:
        pass
    time.sleep(0.01)

# STOPP
def stop():
    # Hraðinn á mótorunum settur í 0
    data = [0, 0, 0, 0]
    try:
        bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)
    except OSError:
        pass
    time.sleep(0.01)

# SNÚAST RÉTTSÆLIS
def rotate_CW(speed):
    # Lætur hann snúast réttsælis á gefnum hraða
    data = [speed, 0, speed, 0]
    try:
        bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)
    except OSError:
        pass
    time.sleep(0.01)

# SNÚAST RANGSÆLIS
def rotate_CCW(speed):
    # Lætur hann snúast rangsælis á gefnum hraða
    data = [speed, 1, speed, 1]
    try:
        bus.write_i2c_block_data(I2C_ADDRESS, 0x00, data)
    except OSError:
        pass
    time.sleep(0.01)

# Snúast um ákveðna gráðu réttsælis
def rotate_by_CW(theta, v=100):
    pi = 3.141592
    x = 0.123
    k = pi * 1/(360*x)
    l = 17.21
    t = k*theta*l/v
    rotate_CW(v)
    time.sleep(t)
    stop()

# Snúast um ákveðna gráðu rangsælis
def rotate_by_CCW(theta, v=100):
    pi = 3.141592
    k = 25*pi/1251
    l = 17.21
    t = k*theta*l/v
    rotate_CCW(v)
    time.sleep(t)
    stop()

# KEYRA
def drive(y_speed, x_speed):
    # Fallið tekur inn lóðréttan og láréttan hraða og stýrir mótorunum eftir því

    curve = 1 - abs(x_speed)/255 # Beygjuhlutfall reiknað
    # Beygjuáttinn ákveðin út frá formerki lárétta hraðans
    if x_speed<0: turn = 2 
    elif x_speed>0: turn = 1
    else: turn = 0
    # Ákveðið hvort fara eigi áfram eða afturábak miðað við formerki lóðrétta hraðans
    if y_speed>0:
        forwards(y_speed, curve, turn)
    elif y_speed<0:
        backwards(abs(y_speed), curve, turn)
    # Ef að lóðréttur hraði er enginn og láréttur!=0 þá snýst hann á staðnum
    elif x_speed!=0:
        if turn == 2:
            rotate_CCW(abs(x_speed))
        elif turn == 1:
            rotate_CW(x_speed)
    else: 
        stop()