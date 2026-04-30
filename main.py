#Konungskóðinn

import time
import motor as m
import skynjarar as s

#m.forwards(50)
#time.sleep(2)
#m.stop()
#intak = input('continue')
#m.forwards(100)
#time.sleep(2)
#m.stop()
#intak = input('continue')
#m.forwards(150)
#time.sleep(2)
#m.stop()
#intak = input('continue')
#m.forwards(200)
#time.sleep(2)
#m.stop()
#intak = input('continue')
#m.forwards(250)
#time.sleep(2)
#m.stop()
#intak = input('continue')



try:
    while True:
        # if s.searching():
        #     m.stop()
        #     time.sleep(1)
        #     m.rotate_CCW(50)
        #     time.sleep(2)
        #     m.stop()
        # else:
        #     m.forwards(100)
        
        # time.sleep(0.2)
        m.rotate_by_CCW(180)
        time.sleep(1)
        m.rotate_by_CW(180)
        time.sleep(1)


except KeyboardInterrupt:
    m.stop()




