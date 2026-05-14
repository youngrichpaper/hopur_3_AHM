#Konungskóðinn
import time
import threading
import multiprocessing
import motor as m
import skynjarar as s
import servo as v
from ps4 import MyController
import camera

camera_queue = multiprocessing.Queue()


def keyra_controller():
    controller.listen(timeout=60)

controller = MyController(camera_queue=camera_queue,interface="/dev/input/js0", connecting_using_ds4drv=False)
#Set upp þræði
fani = threading.Thread(target=v.wave_flag,args=(controller,), daemon=True)
auto = threading.Thread(target=s.skynja,args=(controller,), daemon=True)
controller_thread = threading.Thread(target=keyra_controller, daemon=True)

mynd = multiprocessing.Process(target=camera.live_feed,args=(camera_queue,),daemon=True)

#--------------------------------------------
#Keyrsla
#Auto eða handvirkt
if __name__ == "__main__":

    try:
        # mynd = multiprocessing.Process(
        #     target=camera.live_feed,
        #     args=(camera_queue,),
        #     daemon=True
        # )

        mynd.start()


        controller_thread.start()
        auto.start()
        fani.start()

        while True:

            if not controller.auto_kveikt:
                m.drive(controller.y_speed,controller.x_speed)

            time.sleep(0.05)

    except KeyboardInterrupt:

        print("Stoppar keyrslu")


        m.stop()

        mynd.terminate()

        mynd.join()
