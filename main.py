#Konungskóðinn
# Pakkar teknir inn
import time
import threading
import multiprocessing
from ps4 import MyController, keyra_controller
# Skrár með föllum tekin inn
import motor as m
import skynjarar as s
import servo as v
import camera


# Set upp samskiptaleið milli processa
camera_queue = multiprocessing.Queue()

# Fjarstýringin sett upp með klasanum MyController
controller = MyController(camera_queue=camera_queue,interface="/dev/input/js0", connecting_using_ds4drv=False)

#Set upp þræði
fani = threading.Thread(target=v.wave_flag,args=(controller,), daemon=True)
auto = threading.Thread(target=s.skynja,args=(controller,), daemon=True)
controller_thread = threading.Thread(target=keyra_controller,args=(controller,), daemon=True)
# Set upp process
mynd = multiprocessing.Process(target=camera.live_feed,args=(camera_queue,),daemon=True)
#Byrjað alla þræði og precessa
mynd.start()
controller_thread.start()
auto.start()
fani.start()
#--------------------------------------------
#Keyrsla
#Auto eða handvirkt
if __name__ == "__main__":

    try:
        while True:
            m.drive(controller.y_speed,controller.x_speed)

            time.sleep(0.05)

    except KeyboardInterrupt:

        print("Stoppar keyrslu")


        m.stop()

        mynd.terminate()

        mynd.join()
