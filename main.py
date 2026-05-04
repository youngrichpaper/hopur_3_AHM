#Konungskóðinn
# import pyPS4Controller
import time
import motor as m
import skynjarar as s
import servo as v
# from ps4 import MyController

# controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# # you can start listening before controller is paired, as long as you pair it within the timeout window
# controller.listen(timeout=60)

try:
     while True:
          hindrun_vinstri, hindrun_haegri = s.searching()
          # #Skynjar hindranir
          # if s.searching():
          #     m.stop()
          #     time.sleep(1)
          #     m.rotate_CCW(50)
          #     time.sleep(2)
          #     m.stop()
          # else:
          #     m.forwards(100)
          if hindrun_vinstri:
               m.stop()
               m.rotate_by_CW(60)
               time.sleep(1)
          elif hindrun_haegri:
               m.stop()
               m.rotate_by_CCW(60)
               time.sleep(1)
          else:
               m.forwards(150)

except KeyboardInterrupt:
     m.stop()
    




