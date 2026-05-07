# #Myndavél

from flask import Flask, Response
from picamera2 import Picamera2
import cv2
import time


app = Flask(__name__)

picam2 = Picamera2()


def start_camera():
    config = picam2.create_video_configuration(
        main={
            "size": (1152, 648),
            "format": "RGB888"
        }
    )

    picam2.configure(config)
    picam2.start()
    time.sleep(1)


def generate_frames():
    while True:
        frame = picam2.capture_array()

        frame = cv2.flip(frame, -1)

        ret, buffer = cv2.imencode(".jpg", frame)

        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
        )


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Robot Camera</title>
        </head>
        <body>
            <h1>Live Myndavél</h1>
            <img src="/video_feed" width="840">
        </body>
    </html>
    """


@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

def live_feed():
    # if __name__ == "__main__":
    try:
        start_camera()

        print("Opnaðu þetta í Chrome:")
        print("http://10.98.208.37:5000")

        app.run(
            host="0.0.0.0",
            port=5000,
            debug=False,
            threaded=True
        )

    except KeyboardInterrupt:
        print("Stoppa myndavel")

    finally:
        picam2.stop()
        picam2.close()