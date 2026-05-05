#Konungskóðinn
# import pyPS4Controller
import time
import threading
import os
import motor as m
import skynjarar as s
import servo as v
import speaker as e
# from ps4 import MyController

# controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# # you can start listening before controller is paired, as long as you pair it within the timeout window
# controller.listen(timeout=60)

skanna = threading.Thread(target=v.servo_rotate, daemon=True)
auto = threading.Thread(target=s.skynja, daemon=True)


##################################
try:

     #skanna.start()
     auto.start()

     #skanna.join()
     auto.join()

except KeyboardInterrupt:
     print('Stoppar keyrslu')
     m.stop()
########################################





