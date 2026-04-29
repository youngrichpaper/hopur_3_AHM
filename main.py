#Konungskóðinn

import time
import motor as m
import skynjarar as s

try:
    m.dance()
except KeyboardInterrupt:
    m.stop()