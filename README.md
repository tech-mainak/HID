📟 ESP32 BLE Payload Executor (SPIFFS Script Engine)

A modular ESP32-based BLE HID payload execution framework with SPIFFS script storage, OLED UI, and a lightweight DuckyScript-like interpreter designed for cybersecurity research and embedded systems labs.

⚠️ Educational / Authorized Lab Use Only

🧠 System Overview

This project converts an ESP32 into a:

BLE Keyboard Device
Script Execution Engine
SPIFFS-based Payload Manager
OLED-controlled interface system
🏗️ Architecture Diagram
                 ┌──────────────────────────┐
                 │      Serial Monitor       │
                 │   (Edit / Debug Input)    │
                 └────────────┬─────────────┘
                              │
                              ▼
                ┌───────────────────────────┐
                │        SPIFFS Flash       │
                │  /windows.txt payloads    │
                │  /android.txt             │
                │  /custom.txt              │
                └────────────┬──────────────┘
                             │
                             ▼
         ┌────────────────────────────────────┐
         │     ESP32 Payload Engine           │
         │  (executeLine / parser system)     │
         └────────────┬───────────────────────┘
                      │
          BLE HID      ▼
     ┌──────────────────────────┐
     │   Target Device          │
     │ (Keyboard Input Inject)  │
     └──────────────────────────┘

🚀 Features
📡 BLE Keyboard emulation (ESP32)
📁 SPIFFS file-based payload storage
🧾 DuckyScript-inspired interpreter
🖥️ OLED menu system (128x64 SSD1306)
⌨️ Serial-based file editor
🔁 Line-by-line payload execution
⚡ Lightweight & modular design

🔌 Hardware Pin Connections (ESP32 Wiring)
📟 OLED Display (SSD1306 – I2C)
OLED Pin	ESP32 Pin
VCC	3.3V
GND	GND
SDA	GPIO 21
SCL	GPIO 22
🔘 Push Buttons
Button 1 (Menu / Next)
Button Pin	ESP32 Pin
One side	GPIO 15
Other side	GND
Button 2 (Select / Execute)
Button Pin	ESP32 Pin
One side	GPIO 5
Other side	GND

⚠️ Important Notes
Buttons use INPUT_PULLUP mode → no external resistors required
Pressing button connects GPIO → GND (active LOW)
OLED runs on I2C protocol (default ESP32 pins 21/22)

📊 Wiring Diagram (Simplified)
        ESP32 Dev Board
        ┌──────────────────────┐
        │                      │
        │  GPIO 21 ───── SDA   │──── OLED SDA
        │  GPIO 22 ───── SCL   │──── OLED SCL
        │  3.3V     ───── VCC   │──── OLED VCC
        │  GND      ───── GND   │──── OLED GND
        │                      │
        │  GPIO 15 ───── Button│──── GND
        │  GPIO 5  ───── Button│──── GND
        │                      │
        └──────────────────────┘
🔧 Hardware Requirements
ESP32 Dev Board (ESP-WROOM-32 recommended)
SSD1306 OLED Display (I2C)
2x Push Buttons
USB Cable

💻 Software Requirements
Arduino IDE (latest)
ESP32 Board Support Package
Required Libraries (see below)
⚙️ Installation Guide
1️⃣ Install Arduino IDE

https://www.arduino.cc/en/software

2️⃣ Add ESP32 Board Manager

Go to:

File → Preferences

Add:

https://espressif.github.io/arduino-esp32/package_esp32_index.json

Then:

Tools → Board → Boards Manager
Search: ESP32
Install: ESP32 by Espressif Systems
3️⃣ Select Board
Tools → Board → ESP32 Dev Module
4️⃣ Install Required Libraries

Install via Library Manager:

Adafruit SSD1306
Adafruit GFX
SPIFFS (built-in)
Wire (built-in)
ESP32 BLE Keyboard
https://github.com/T-vK/ESP32-BLE-Keyboard
📁 SPIFFS File System
Default Structure
/windows.txt
/android.txt
/iphone.txt
/custom.txt

Each file contains script instructions executed line-by-line.

📦 Payload Flow Diagram
      User Input (Serial / File Edit)
                    │
                    ▼
        ┌─────────────────────┐
        │   SPIFFS Storage    │
        └─────────┬───────────┘
                  ▼
     ┌──────────────────────────┐
     │   executeLine(parser)    │
     └─────────┬────────────────┘
               ▼
     BLE Keyboard Injection Layer
               ▼
        Target Device Input
✍️ Payload Syntax
Command	Description
STRING text	Type characters
NUMBER 1002	Type digits
DELAY 1000	Wait in milliseconds
ENTER	Press Enter
TAB	Press Tab
ESC	Escape key
UP/DOWN/LEFT/RIGHT	Arrow keys
🧪 Example Payload
STRING Hello World
ENTER
DELAY 1000
NUMBER 1002
ENTER
🧾 File Editing (SPIFFS)
📌 Enter Edit Mode
EDIT /windows.txt
📌 Add Payload Lines
STRING Hello
DELAY 500
NUMBER 1002
ENTER
📌 Finish Editing
END
👀 File Operations
List files
LIST
Show file content
SHOW /windows.txt
Delete line
DEL /windows.txt 2
Clear file
CLEAR /windows.txt
🎮 UI Flow
Boot ESP32
   │
   ▼
OLED Menu
   │
   ├── Windows Payload
   ├── Android Payload
   ├── iPhone Payload
   └── Custom Payload
   │
   ▼
BLE Connect
   │
   ▼
Execute Script
⚠️ Safety Notice

This project is intended strictly for:

✔ Cybersecurity research
✔ Embedded systems learning
✔ Authorized penetration testing labs

❌ Do NOT use on unauthorized systems

🔧 Troubleshooting
BLE not connecting
Re-pair device: “ESP Keyboard”
Restart ESP32
SPIFFS errors
SPIFFS.begin(true);
Upload issues
Ensure correct board selected:
ESP32 Dev Module
🚀 Future Enhancements
🌐 Web-based payload editor
📱 Mobile control interface
🔐 Encrypted SPIFFS storage
🧠 Advanced scripting engine (variables, loops)
🖥️ OLED file manager UI
👨‍💻 Author

Built for embedded cybersecurity experimentation and research.
