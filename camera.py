# #Myndavél

from flask import Flask, Response, send_from_directory
from picamera2 import Picamera2
from datetime import datetime
import os
import cv2
import time


app = Flask(__name__)

picam2 = None


def start_camera():
    global picam2

    picam2 = Picamera2()
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

        ret, buffer = cv2.imencode(".jpg", frame)

        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
        )


@app.route("/pictures/<filename>")
def pictures(filename):
    return send_from_directory(
        "/home/hopur_3/Pictures",
        filename
    )

@app.route("/view/<filename>")
def view_image(filename):

    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>{filename}</title>
        </head>

        <body>

            <h1>{filename}</h1>

            <img src="/pictures/{filename}" width="1000">

            <br><br>

            <a href="/">Til baka</a>

        </body>
    </html>
    """
@app.route("/image_list")
def image_list():

    folder = "/home/hopur_3/Pictures"

    files = sorted(
        os.listdir(folder),
        reverse=True
    )

    image_links = "<ul>"

    for file in files:
        image_links += f'''
            <li>
                <a href="/view/{file}">
                    {file}
                </a>
            </li>
        '''

    image_links += "</ul>"

    return image_links

@app.route("/")
def home():

    folder = "/home/hopur_3/Pictures"

    files = sorted(
        os.listdir(folder),
        reverse=True
    )

    image_links = ""

    for file in files:
        image_links += f'''
            <li>
                <a href="/view/{file}">
                    {file}
                </a>
            </li>
        '''

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Robot Camera</title>
    </head>

    <body>

        <h1>Live Myndavél</h1>

        <img src="/video_feed" width="840">

        <h2>Vistaðar myndir</h2>

        <div id="image-list">
            {image_links}
        </div>

    <script>

    function refreshImages() {{
        fetch('/image_list')
            .then(response => response.text())
            .then(data => {{
                document.getElementById('image-list').innerHTML = data;
            }});
    }}

    setInterval(refreshImages, 10000);

    </script>

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
            use_reloader=False,
            threaded=True
        )

    except KeyboardInterrupt:
        print("Stoppa myndavel")

    finally:
        picam2.stop()
        picam2.close()

def take_picture():
    folder = "/home/hopur_3/Pictures"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"mynd_{timestamp}.jpg"
    file_path = os.path.join(folder, filename)
    picam2.capture_file(file_path)
    print('mynd tekin')