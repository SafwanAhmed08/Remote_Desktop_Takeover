---

# Remote Desktop Takeover

A lightweight Python-based application to simulate remote desktop control using sockets and GUI events. The server provides a virtual trackpad interface, and the client executes mouse and keyboard events locally using `pyautogui`.

---

## Features

* **Remote Mouse Control**: Move the mouse on the client system by tracking server-side cursor motion.
* **Remote Click Execution**: Simulate left-clicks from the server on the client machine.
* **Remote Keystroke Typing**: Capture and send keystrokes from the server to simulate typing on the client.

---

## How It Works

* The **server** starts a GUI window (trackpad) and listens for motion, click, and key events.
* The **client** connects via socket, receives instructions (cursor position, clicks, keys), and executes them using `pyautogui`.

---

## Requirements

* Python 3.x
* `pyautogui`
* `tkinter` (included with standard Python)
* Works on LAN (both devices must be on the same network)

---

## Setup Instructions

### 1. Install dependencies (only required on the **client**):

```bash
pip install pyautogui
```

### 2. Run the Server

```bash
python server.py
```

* A popup will display the Host IP and Port to connect to.
* A GUI window will open. Moving your mouse within this window will send cursor commands to the client.

### 3. Run the Client (on the system to be controlled)

```bash
python client.py
```

* Enter the Host and Port shown on the server when prompted.
* The client will then begin executing motion, click, and keystroke commands sent by the server.

---

## Notes

* The cursor motion is scaled for better visibility.
* The `pyautogui` library is used to simulate mouse and keyboard control on the client.
* This is a basic implementation meant for educational or prototype purposes.

---

## Security Disclaimer

This tool does **not** implement authentication, encryption, or access control. It should **not** be used over public networks or the internet. Only run in trusted local environments.

---
