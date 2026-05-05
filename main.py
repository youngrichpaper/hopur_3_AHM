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

# controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# # you can start listening before controller is paired, as long as you pair it within the timeout window
# controller.listen(timeout=60)

# skanna = threading.Thread(target=v.servo_rotate, daemon=True)

x_press = MyController.on_x_press
c_press = MyController.on_circle_press

auto = threading.Thread(target=s.skynja, daemon=True)


#--------------------------------------------
#Autonomous keyrsla
try:
     while True:
          if x_press:
               #skanna.start() #Fyrir servo (hreyfing)
               auto.start()

               #skanna.join()
               auto.join()
          if c_press:
               x_press = False
          

         

except KeyboardInterrupt:
     print('Stoppar keyrslu')
     m.stop()
#--------------------------------------------





