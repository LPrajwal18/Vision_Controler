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

```bash
python eye_control.py
Controls:

Cursor Movement: Move your eyes to move the cursor.

Left Click: Blink your left eye.

Right Click: Blink your right eye.

Zoom In/Out: Bring your eyes closer or move them apart.

Screenshot: Close both eyes for at least 2.5 seconds.

Exit: Press q to quit the application.

Configuration

Adjust the following parameters in eye_control.py to tailor behavior:

BLINK_THRESHOLD: Sensitivity for blink detection (lower = more sensitive).

ZOOM_SENSITIVITY: Minimum eye-distance change to trigger zoom.

CLICK_COOLDOWN: Time (seconds) between clicks to prevent rapid-fire actions.

ZOOM_COOLDOWN: Time (seconds) between zoom actions.

SCREENSHOT_DURATION: Duration (seconds) both eyes must be closed to capture a screenshot.

Roadmap

Calibration Routine: Implement a quick calibration for each user to adjust thresholds.

GUI Overlay: On-screen indicators showing eye status, clicks, and zoom level.

Multi-Face Support: Handle multiple faces or toggle between users.

Cross-Platform Packaging: Create installers for Windows, macOS, and Linux.

Integration with Other Accessibility Tools: Combine with voice commands or switch devices.

Troubleshooting & FAQs

Q: Camera not detected?

Ensure no other application is using the webcam. Verify cv2.VideoCapture(0) index or try other indices.

Q: Blinks not registering?

Adjust BLINK_THRESHOLD in code. Check lighting conditions.

Q: Zoom too sensitive/insensitive?

Modify ZOOM_SENSITIVITY and ZOOM_COOLDOWN values.

Q: Application lags?

Increase frame_skip_rate or reduce video resolution.

Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeature).

Commit your changes (git commit -m 'Add YourFeature').

Push to the branch (git push origin feature/YourFeature).

Open a Pull Request.

Please ensure your code follows the existing style and includes relevant documentation and tests where applicable.

Support

For questions, issues, or requests, please open an issue on GitHub or contact the maintainer at your.email@example.com.
