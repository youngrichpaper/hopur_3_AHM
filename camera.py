# #Myndavél

from flask import Flask, Response, send_from_directory, redirect
from picamera2 import Picamera2
from datetime import datetime
import os
import cv2
import time
import threading


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

    html = ""

    for file in files:

        html += f"""

        <div class="tile">

            <a href="/view/{file}">
                <img
                    src="/pictures/{file}"
                    class="thumb"
                >
            </a>

            <p>{file}</p>

            <a href="/delete/{file}">
                <button>Eyða</button>
            </a>

        </div>
        """

    return html

@app.route("/gallery")
def gallery():

    return """
    <!DOCTYPE html>

    <html>

    <head>

        <title>Myndasafn</title>

        <style>

            body {
                font-family: Arial;
                background: #111;
                color: white;
                margin: 20px;
            }

            .grid {

                display: grid;

                grid-template-columns:
                    repeat(auto-fill, minmax(250px, 1fr));

                gap: 20px;
            }

            .tile {

                background: #222;

                padding: 10px;

                border-radius: 10px;

                text-align: center;
            }

            .thumb {

                width: 100%;

                border-radius: 10px;
            }

            button {

                margin-top: 10px;

                padding: 8px 14px;

                border: none;

                border-radius: 5px;

                cursor: pointer;
            }

            a {
                color: white;
                text-decoration: none;
            }

        </style>

    </head>

    <body>

        <h1>Vistaðar myndir</h1>

        <a href="/">Til baka í myndavél</a>

        <br><br>

        <div
            id="gallery"
            class="grid">
        </div>

        <script>

        function refreshGallery() {

            fetch("/image_list")

            .then(response => response.text())

            .then(data => {

                document.getElementById(
                    "gallery"
                ).innerHTML = data;
            });
        }

        refreshGallery();

        setInterval(refreshGallery, 5000);

        </script>

    </body>

    </html>
    """

@app.route("/delete/<filename>")
def delete_image(filename):

    folder = "/home/hopur_3/Pictures"

    file_path = os.path.join(folder, filename)

    if os.path.exists(file_path):

        os.remove(file_path)

        print(f"Eyddi: {filename}")

    return redirect("/gallery")

# @app.route("/")
# def home():

#     return """

#     <!DOCTYPE html>

#     <html>

#     <head>
#         <title>Robot Camera</title>
#     </head>

#     <body>

#         <h1>Live Myndavél</h1>

#         <img
#             src="/video_feed"
#             width="840"
#         >

#         <br><br>

#         <a href="/gallery">

#             <button>
#                 Opna myndasafn
#             </button>

#         </a>

#     </body>

#     </html>
#     """


@app.route("/")
def home():

    return """

    <!DOCTYPE html>

    <html>

    <head>

        <title>Robot Camera</title>

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>

            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: white;
            }

            .container {
                max-width: 1200px;
                margin: auto;
                padding: 20px;
            }

            .header {
                text-align: center;
                margin-bottom: 30px;
            }

            .header h1 {
                font-size: 3rem;
                margin-bottom: 10px;
            }

            .header p {
                color: #cbd5e1;
                font-size: 1.1rem;
            }

            .video-card {
                background: #1e293b;
                border-radius: 20px;
                padding: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            }

            .video-stream {
                width: 100%;
                border-radius: 15px;
                border: 4px solid #334155;
            }

            .controls {
                margin-top: 25px;
                display: flex;
                gap: 15px;
                flex-wrap: wrap;
                justify-content: center;
            }

            .button {
                background: #2563eb;
                color: white;
                padding: 14px 24px;
                border-radius: 12px;
                text-decoration: none;
                font-size: 1rem;
                font-weight: bold;
                transition: 0.2s;
                display: inline-block;
            }

            .button:hover {
                background: #1d4ed8;
                transform: scale(1.03);
            }

            .status-grid {
                margin-top: 30px;
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
            }

            .status-card {
                background: #1e293b;
                padding: 20px;
                border-radius: 18px;
                text-align: center;
                box-shadow: 0 5px 20px rgba(0,0,0,0.3);
            }

            .status-card h2 {
                margin: 0;
                font-size: 1.2rem;
                color: #93c5fd;
            }

            .status-card p {
                margin-top: 10px;
                font-size: 1rem;
                color: #e2e8f0;
            }

            .footer {
                margin-top: 40px;
                text-align: center;
                color: #94a3b8;
                font-size: 0.9rem;
            }

        </style>

    </head>

    <body>

        <div class="container">

            <div class="header">
                <h1>Myndavél</h1>
            </div>

            <div class="video-card">

                <img
                    src="/video_feed"
                    class="video-stream"
                >

                <div class="controls">

                    <a href="/gallery" class="button">
                        Skoða myndir
                    </a>

                </div>

            </div>

        </div>

    </body>

    </html>
    """
@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )



def run_flask():

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False,
        threaded=True
    )


def live_feed(command_queue):

    try:

        start_camera()

        flask_thread = threading.Thread(
            target=run_flask,
            daemon=True
        )

        flask_thread.start()

        print("Opnaðu:")
        print("http://10.98.208.37:5000")

        while True:

            if not command_queue.empty():

                command = command_queue.get()

                if command == "take_picture":

                    save_picture()

            time.sleep(0.05)

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

def save_picture():

    folder = "/home/hopur_3/Pictures"

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = f"mynd_{timestamp}.jpg"

    file_path = os.path.join(
        folder,
        filename
    )

    picam2.capture_file(file_path)

    print(f"Mynd vistuð: {filename}")