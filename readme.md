# 📱 QR Code Generator App (Python)

A feature-rich, customizable **QR Code Generator application** built using Python. This repository contains the **Latest Modern GUI** version (built with `CustomTkinter`), **Classic GUI** legacy versions (built with native `Tkinter`), and a **CLI Version** for terminal usage.

The application allows users to generate custom-styled QR codes with personalized pattern colors, background colors, high-capacity error correction, and instant live previews.

---

## ✨ Features

### 🌟 New Modern GUI (Latest Version)
* **Modern UI & Themes:** Sleek CustomTkinter interface supporting **Dark Mode**, **Light Mode**, and **System Default** themes.
* **Color Picker Wheel:** Built-in interactive color picker (`CTkColorPicker`) to easily select custom pattern and background colors.
* **Icon-enhanced Controls:** Visual icon buttons for Generate, Clear, Save, Theme toggle, and Help.
* **Input Validation:** Built-in color verification (`colour` library) and input sanitization to prevent errors.
* **Pop-up Notifications:** Stylish alert and help dialogues (`CTkMessagebox`).
* **Live QR Preview:** Instant high-resolution preview of the generated QR code before saving.
* **Export Options:** Save generated QR codes as `.png` or `.jpg` files in any directory.
* **Error Correction:** Uses High Level Error Correction (`ERROR_CORRECT_H` ~30% recovery) so QR codes remain readable even if partially damaged or obscured.

### 🏛️ Classic GUI & CLI (Legacy & Terminal Versions)
* **Classic GUI:** Lightweight interface built using Python's native `Tkinter` (`Old UI/main.py`).
* **CLI Version:** Command-line script (`Old UI/QR Generator CLI.py`) for generating QR codes directly in the terminal.
* Supports custom color choices and text input for color names or hex codes.

---

## 📋 Prerequisites & System Requirements

Before running the application, ensure you have Python installed on your system.

* **Python Version:** Python 3.8 or higher (Python 3.10+ recommended).

### 📦 Required Python Packages

The application relies on the third-party libraries listed in `requirements.txt`:

| Package | Purpose | Used In |
| :--- | :--- | :--- |
| `customtkinter` | Modern UI framework and dark/light theme support | Modern GUI |
| `CTkColorPicker` | Interactive color wheel popup | Modern GUI |
| `CTkMessagebox` | Modern notification dialogs | Modern GUI |
| `qrcode` | QR code generation engine | Modern GUI, Classic GUI & CLI |
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

2. **Set Up Virtual Environment & Install Dependencies:**

   ```bash
   # 1. Create a virtual environment named 'venv'
   python -m venv venv

   # 2. Activate it 
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate

   # 3. Install all packages safely inside the environment
   pip install -r requirements.txt
   ```

---

## 🚀 How to Run the Application

### 1️⃣ Run Modern GUI (Latest Version - Recommended)
Execute the main script in the `Modern UI` directory:
```bash
python "Modern UI/main.py"
```
