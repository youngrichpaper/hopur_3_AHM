# #Myndavél

# import io
# # import picamera
# from flask import Flask, Response
# from picamera2 import Picamera2

from flask import Flask, Response
from picamera2 import Picamera2
import cv2
import time

# app = Flask(__name__)
# picam2 = Picamera2()
# picam2.configure(picam2.create_video_configuration(main={"size":(640, 480)}))
# picam2.start()

# def generate_frames():
#     while True:
#         frame = picam2.capture_array()
#     # with picamera.PiCamera() as camera:
#     #     camera.resolution = (640, 480)
#     #     camera.framerate = 24
#     #     stream = io.BytesIO()

#     #     for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
#     #         stream.seek(0)
#     #         yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + stream.read() +b'\r\n'
#     #         stream.seek(0)
#     #         stream.truncate()
#         yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#         pass

# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
# if __name__ == '__main__':
#     app.run(host= '0.0.0.0', port=5000) # , threaded=True)

app = Flask(__name__)

picam2 = Picamera2()


def start_camera():
    config = picam2.create_video_configuration(
        main={"size": (640, 480), "format": "RGB888"}
    )
    picam2.configure(config)
    picam2.start()
    time.sleep(1)

    print("Opnaðu þetta í Chrome:")
    print("http://10.98.208.37:5000")

    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)


def generate_frames():
    while True:
        frame = picam2.capture_array()

        ret, buffer = cv2.imencode(".jpg", frame)

        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
        )


@app.route("/")
def index():
    return """
    <html>
        <body>
            <h1>Live myndavel</h1>
            <img src="/video_feed" width="640">
        </body>
    </html>
    """


@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    start_camera()