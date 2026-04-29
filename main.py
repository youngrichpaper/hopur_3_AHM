#Konungskóðinn

import time
import motor as m

try:
    m.dance()
except KeyboardInterrupt:
    m.stop()