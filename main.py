#Konungskóðinn

import time
import motor as m
import skynjarar as s

try:
    m.dance()
except KeyboardInterrupt:
    m.stop()

while True:
    if s.searching():
        m.stop()
        time.sleep(1)
        m.rotate_CW(50)
        time.sleep(4)
        m.stop()
        time.sleep(1)
        m.forwards(100)

    else:
        continue

    


