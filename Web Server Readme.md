# iOS Lock Screen Simulation Web Server

A minimalist, fullscreen HTML5/Flask web application replicating a native iOS style passcode lock screen interface. Keys pressed are dynamically logged via a Flask backend and synced using WebSockets.

## 📂 Project Structure

Ensure your directory matches this layout for the application to load static assets correctly:

```text
numpad-web/
├── app.py
├── logs.txt              # Automatically created when keys are pressed
├── templates/
│   └── index.html        # Main frontend UI
└── static/
    └── wallpaper.jpg     # Background image (User provided)

🖼️ Wallpaper Setup
Create a directory named static if it does not exist inside your project folder.

Choose any background image you like, rename it exactly to wallpaper.jpg, and place it inside that static folder.

The image will automatically adapt to your screen using CSS cover positioning.

🚀 Installation & Running on Linux
Follow these terminal commands from your Kali Linux desktop to set up the environment and run the server.

1. Navigate to your project folder
Bash
cd /home/kali/Desktop/numpad-web/
2. Install dependencies
Ensure you have Python 3, Flask, and Flask-SocketIO installed:

Bash
pip3 install flask flask-socketio
3. Run the application
Start the local server by running the main execution script:

Bash
python3 app.py
4. Access the web app
Open your web browser (on your desktop or mobile device connected to the same network) and go to:

Local access: http://127.0.0.1:5000

Network access: http://<your-kali-ip-address>:5000

📝 Features & Notes
Fullscreen Mode: On mobile or desktop, the web application attempts to trigger a clean fullscreen experience right upon the first user interaction event.

Logging Engine: Every number pressed hits the backend API via asynchronous JavaScript fetching and logs groupings into logs.txt synchronously.

Redirection: Entering a 4-digit passcode automatically completes the sequence execution, routing the user to the configured YouTube landing target.
