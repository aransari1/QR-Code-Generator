# 📱 QR Code Generator App (Python)

A feature-rich, customizable **QR Code Generator application** built using Python. This repository contains both the **Latest Modern GUI** version (built with `CustomTkinter`) and the **Classic GUI** legacy versions (built with native `Tkinter`).

The application allows users to generate custom-styled QR codes with personalized pattern colors, background colors, high-capacity error correction, and instant live previews.

---

## ✨ Features

### 🌟 New Modern GUI (Latest Version)
* **Modern UI & Themes:** Sleek CustomTkinter interface supporting **Dark Mode**, **Light Mode**, and **System Default** themes.
* **Color Picker Wheel:** Built-in interactive color picker (`CTkColorPicker`) to easily select custom pattern and background colors.
* **Input Validation:** Built-in color verification (`colour` library) and input sanitization to prevent errors.
* **Pop-up Notifications:** Stylish alert and help dialogues (`CTkMessagebox`).
* **Live QR Preview:** Instant high-resolution preview of the generated QR code before saving.
* **Export Options:** Save generated QR codes as `.png` or `.jpg` files in any directory.
* **Error Correction:** Uses High Level Error Correction (`ERROR_CORRECT_H` ~30% recovery) so QR codes remain readable even if partially damaged or obscured.

### 🏛️ Classic GUI (Legacy Versions)
* Lightweight interface built using Python's native `Tkinter`.
* Supports basic color chooser dialogues and text input for Hex/Color names.
* Includes historical iterations of the app (`GUI 1.0`, `GUI 2.0`, `GUI 4.0`, and `QR Generator GUI.py`).

---

## 📋 Prerequisites & System Requirements

Before running the application, ensure you have Python installed on your system.

* **Python Version:** Python 3.8 or higher (Python 3.10+ recommended).

### 📦 Required Python Packages

The application relies on the following third-party libraries:

| Package | Purpose | Used In |
| :--- | :--- | :--- |
| `customtkinter` | Modern UI framework and dark/light theme support | Modern GUI |
| `CTkColorPicker` | Interactive color wheel popup | Modern GUI |
| `CTkMessagebox` | Modern notification dialogs | Modern GUI |
| `qrcode` | QR code generation engine | Modern & Classic GUI |
| `Pillow` (`PIL`) | Image processing and canvas rendering | Modern & Classic GUI |
| `colour` | Color name & Hex validation | Modern & Classic GUI |

> **Note for Linux Users:** If you are running Linux, `tkinter` might not come pre-installed with Python. Install it using your system package manager:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## 🛠️ Installation & Setup

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/your-username/QR-Code-Generator-App-using-Python.git
   cd QR-Code-Generator-App-using-Python
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   * **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   * **macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies:**
   Run the following command to install all required packages at once:
   ```bash
   pip install customtkinter CTkColorPicker CTkMessagebox qrcode pillow colour
   ```

---

## 🚀 How to Run the Application

### 1️⃣ Run Modern GUI (Latest Version - Recommended)
Navigate to the `QR Generator with Modern UI` directory and execute the main script:
