# XGO Mini 2 – Face Recognition & Tracking System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Platform](https://img.shields.io/badge/Platform-XGO%20Mini%202-orange)
![License](https://img.shields.io/badge/License-MIT-green)

### Intelligent real-time face tracking, recognition, and alert system for the XGO Mini 2 robotic dog.

---

## Overview
This project enables the **XGO Mini 2** robot to:
- Detect and recognize faces using its built-in AI and camera.
- Follow faces by turning and adjusting its position automatically.
- Display detection status on the robot’s screen in real time.
- Capture and securely log images of unknown faces.
- Send email alerts with attached images when unrecognized faces appear.

Built with Python, OpenCV, and the official XGO libraries.

---

## Features
- Real-time face tracking using the built-in `face_detect()` function from `xgoedu`.
- Integrated camera control for automatic photo capture.
- On-screen status display through the robot’s LCD.
- Secure logging of unrecognized faces organized by date.
- Email alerts with photo attachments via secure Gmail app passwords.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/XGO-Mini-Face-Recognition.git
cd XGO-Mini-Face-Recognition
