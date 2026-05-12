#Konungskóðinn
import pyPS4Controller
import time
import threading
import multiprocessing
import os
import motor as m
import skynjarar as s
import servo as v
import speaker as e
from ps4 import MyController
import camera


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)


def keyra_controller():
    controller.listen(timeout=60)

#Set upp þræði
fani = threading.Thread(target=v.wave_flag, daemon=True)
auto = threading.Thread(target=s.skynja, daemon=True)
mynd = multiprocessing.Process(target=camera.live_feed, daemon=True)
controller_thread = threading.Thread(target=keyra_controller, daemon=True)



#--------------------------------------------
#Keyrsla
#Auto eða handvirkt
try:
    mynd.start()
    time.sleep(0.05)
    controller_thread.start()
    # auto.start()
    fani.start()
    while True:
        if not s.auto_kveikt:
            m.drive(controller.y_speed, controller.x_speed) 
        else: 
            s.skynja()
        time.sleep(0.05)


except KeyboardInterrupt:
    print("Stoppar keyrslu")
    s.auto_kveikt = False
    m.stop()
#--------------------------------------------





