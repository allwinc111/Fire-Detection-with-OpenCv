# 🔥 Fire Detection and Alert System

A real-time fire detection and alert system using Python, OpenCV, and a Haar Cascade classifier. When fire is detected via webcam, it triggers an alarm and sends an email alert.

---

## 🚀 Features

- 🔍 Detects fire in live webcam feed using Haar Cascade
- 🔊 Plays a fire alarm sound on detection
- 📧 Sends an alert email (once per session)
- 🎥 Displays live video with highlighted fire areas

---

## 🛠️ Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- playsound
- smtplib (built-in)
- threading (built-in)

Install required packages:
```bash
pip install opencv-python playsound
