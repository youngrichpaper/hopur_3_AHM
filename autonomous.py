import skynjarar as s
import motor as m

try:
    if not s.searching():
        m.forwards(150)
    else:
        m.stop()
        m.rotate_by_CW(90)

except KeyboardInterrupt:
    m.stop()

