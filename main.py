#Konungskóðinn
import pyPS4Controller
import time
import threading
import os
import motor as m
import skynjarar as s
import servo as v
import speaker as e
from ps4 import MyController
import camera


# skanna = threading.Thread(target=v.servo_rotate, daemon=True)
# auto = threading.Thread(target=s.skynja, daemon=True)

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
auto = threading.Thread(target=s.skynja, daemon=True)
mynd = threading.Thread(target=camera, daemon=True)

def keyra_controller():
    controller.listen(timeout=60)


controller_thread = threading.Thread(target=keyra_controller, daemon=True)



#--------------------------------------------
#Autonomous keyrsla
try:
    auto.start()
    controller_thread.start()
    mynd.start()
    while True:
        if not s.auto_kveikt:
            m.drive(controller.y_speed, controller.x_speed)
        
        time.sleep(0.05)


except KeyboardInterrupt:
    print("Stoppar keyrslu")
    s.auto_kveikt = False
    m.stop()
#--------------------------------------------





