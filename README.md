# Vision Controller: Eye-Tracking Mouse Interface

Empower your computer interaction through eye movements and blinks.

## Table of Contents
- [Overview](#overview)
- [About](#about)
- [Features](#features)
- [Use Cases](#use-cases)
- [Real-Life Examples](#real-life-examples)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Configuration](#configuration)
- [Roadmap](#roadmap)
- [Troubleshooting & FAQs](#troubleshooting--faqs)
- [Contributing](#contributing)
- [Support](#support)

## Overview
Vision Controller is an AI-driven system designed to provide hands-free computer control using eye-tracking and blink detection. Leveraging real-time computer vision, it translates gaze direction into cursor movement, blinks into mouse clicks, eye-distance changes into zoom actions, and prolonged eye closure into screenshots. The primary motivation is to empower individuals without use of their hands to fully interact with computers.

## About
Developed at the intersection of human‑computer interaction and accessibility, Vision Controller offers an alternative input modality for scenarios where traditional devices (keyboard, mouse, touch) are impractical or inaccessible. This project showcases how lightweight machine learning pipelines can run in real-time on consumer hardware, enabling intuitive, low-latency interaction without specialized equipment.

## Features
- **Gaze-Based Cursor Control**: Seamlessly move the cursor by tracking your eye movements.
- **Blink Detection for Clicks**: Perform left or right clicks with simple blinks.
- **Zoom Control**: Adjust zoom level based on the distance between your eyes.
- **Screenshot Capture**: Automatically capture a screenshot after closing both eyes for 2.5 seconds.
- **Optimized Performance**: Frame-skipping strategy balances responsiveness and CPU load.
- **Customizable Thresholds**: Easily tune blink sensitivity and zoom sensitivity in code.

## Use Cases
- **Accessibility for Limb Loss**: Enable users without hands or with motor impairments to navigate and interact with software independently.
- **Assistive Technology**: Support individuals with conditions like ALS or spinal cord injuries to regain computer access.
- **Hands-Free Operation**: Ideal for sterile environments (labs, medical) or industrial settings where touch-free control reduces contamination risk.
- **Presentations & Demos**: Advance slides, zoom in on details, or click links without a clicker or keyboard.
- **Gaming & AR/VR**: Prototype gaze-based controls for immersive experiences.
- **Public Displays & Kiosks**: Enable touchless navigation on information kiosks, ATMs, or museum exhibits.

## Real-Life Examples
- **Users without Hands**: Individuals born without limbs or who have lost hand function can browse the web, write documents, or interact with social media solely through eye movements and blinks.
- **Assistive Technology for ALS Patients**: A user with amyotrophic lateral sclerosis navigates email and web pages using only eye movements and blinks, regaining independence.
- **Surgical Environments**: Surgeons in operating rooms control imaging tools and patient records without touching screens, maintaining sterility.
- **Museum Interactive Exhibits**: Visitors explore digital exhibits by gazing at points of interest, enhancing engagement without physical contact.
- **Presentation Control in Conferences**: A speaker advances slides and zooms into charts during a keynote presentation without using a clicker or keyboard.
- **Quality Control in Manufacturing**: Technicians review real-time data on large displays by looking at specific dashboards, improving workflow efficiency.

## Tech Stack
- **Python 3.8+**
- **OpenCV**: Real-time video capture and processing
- **MediaPipe**: Facial landmark detection
- **PyAutoGUI**: Mouse and keyboard automation
- **Threading**: Background frame processing

## Prerequisites
- **Python 3.8 or higher**
- **pip** (Python package installer)
- **A webcam**

## Usage
Run the application:

'''bash
python eye_control.py
'''

# Eye-Controlled Mouse & Interaction System

A Python-based application using OpenCV, MediaPipe, and PyAutoGUI that enables users to control their computer using only their eye movements and gestures — designed for accessibility and hands-free interaction.

---

## 🎮 Controls

| Action              | Trigger                                  |
|---------------------|-------------------------------------------|
| **Cursor Movement** | Move your eyes around                     |
| **Left Click**      | Blink your **left eye**                   |
| **Right Click**     | Blink your **right eye**                  |
| **Zoom In/Out**     | Bring eyes closer / move them apart       |
| **Screenshot**      | Close **both eyes** for at least 2.5 sec  |
| **Exit**            | Press `q`                                 |

---

## ⚙️ Configuration

To tailor the application’s behavior, you can modify the following parameters in `eye_control.py`:

- `BLINK_THRESHOLD`: Controls sensitivity for blink detection (lower = more sensitive).
- `ZOOM_SENSITIVITY`: Minimum eye-distance change needed to trigger zoom.
- `CLICK_COOLDOWN`: Time (in seconds) between click events.
- `ZOOM_COOLDOWN`: Time (in seconds) between zoom actions.
- `SCREENSHOT_DURATION`: Duration (in seconds) both eyes must be closed for a screenshot to trigger.

---

## 🗺️ Roadmap

- ✅ Cursor control with eye tracking
- ✅ Blink-based click detection
- ✅ Eye-distance-based zoom
- ✅ Screenshot functionality via eye closure
- [ ] Calibration routine for individual users
- [ ] On-screen GUI overlay (eye status, zoom level, click indicators)
- [ ] Multi-face support and user toggle
- [ ] Voice command and accessibility tool integration
- [ ] Cross-platform packaging for Windows, macOS, and Linux

---

## ❓ Troubleshooting & FAQs

**Q: Camera not detected?**  
🔧 Make sure no other application is using the webcam. Try changing the index in `cv2.VideoCapture(0)` to `1`, `2`, etc.

**Q: Blinks not registering?**  
🔧 Adjust `BLINK_THRESHOLD` in the code and ensure the lighting is adequate.

**Q: Zoom too sensitive or not triggering?**  
🔧 Modify `ZOOM_SENSITIVITY` and `ZOOM_COOLDOWN`.

**Q: Application is lagging?**  
🔧 Reduce the webcam resolution or increase `frame_skip_rate`.

---

## 📬 Support

For issues or feature requests:

- 📌 Open a GitHub Issue
- 📧 Contact the maintainer: `lprajwal18@gmail.com`

---



Made with ❤️ to empower and enable eye-based control for everyone.

