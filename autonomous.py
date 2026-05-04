import skynjarar as s
import motor as m

try:
    if not s.searching():
        m.forwards()

except KeyboardInterrupt:
    m.stop()

