from flask import Flask, render_template, request
from flask_socketio import SocketIO
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

LOG_FILE = "logs.txt"
buffer = ""  # stores digits before grouping

def write_log(data):
    with open(LOG_FILE, "a") as f:
        f.write(data)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/press", methods=["POST"])
def press():
    global buffer

    key = request.json.get("key")

    if key is None:
        return {"status": "error"}, 400

    # Only group numeric keys
    if key.isdigit():
        buffer += key

        # Create 4-digit groups
        if len(buffer) == 4:
            write_log(buffer + " ")
            socketio.emit("update", {"log": get_log()})
            buffer = ""

    else:
        # special keys like * #
        write_log(key)
        socketio.emit("update", {"log": get_log()})

    return {"status": "ok"}

@app.route("/log")
def get_log():
    if not os.path.exists(LOG_FILE):
        return ""
    with open(LOG_FILE, "r") as f:
        return f.read()

@app.route("/clear", methods=["POST"])
def clear():
    global buffer
    buffer = ""
    open(LOG_FILE, "w").close()
    socketio.emit("update", {"log": ""})
    return {"status": "cleared"}

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
