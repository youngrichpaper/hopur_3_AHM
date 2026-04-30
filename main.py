#Konungskóðinn
import pyPS4Controller
import time
import motor as m
import skynjarar as s
import servo as v

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
        #Skynjar hindranir
         if s.searching():
             m.stop()
             time.sleep(1)
             m.rotate_CCW(50)
             time.sleep(2)
             m.stop()
         else:
             m.forwards(100)
        
        #Snúningur
        # time.sleep(0.2)
        #m.rotate_by_CW(180)
        #time.sleep(1)
        #m.rotate_by_CW(180)
        #time.sleep(1)

        #Servoar
        #v.rotate_s1(180)
        #v.rotate_s2(180)
        #time.sleep(1)
        #v.rotate_s1(0)
        #v.rotate_s2(0)
        #time.sleep(2)
        #v.rotate_s1(90)
        #v.rotate_s2(90)



except KeyboardInterrupt:
    m.stop()




