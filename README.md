
# SAFEAI – AI Emergency & Safety Assistant

SAFEAI is an AI-powered emergency and safety assistant designed to help users analyze potentially dangerous situations and receive appropriate safety guidance.

## Features

- 🛡️ Analyze emergency situations
- 🚨 Classify situations as LOW, MEDIUM, or HIGH risk
- 🤖 AI-powered safety recommendations
- 🎤 Voice input for describing situations
- 📍 Location sharing with Google Maps
- 📩 Emergency message generation for trusted contacts
- 🆘 SOS emergency options
- ⚡ Simple and user-friendly interface

## Tech Stack

- Python
- Flask
- OpenAI API
- HTML
- CSS
- JavaScript

## Project Structure

```text
SAFEAI/
├── app.py
├── requirements.txt
├── start_safeai.bat
├── .gitignore
├── static/
└── templates/
```

## Installation & Setup

### Prerequisites

- Python 3.10 or later
- Git

### 1. Clone the repository

```bash
git clone https://github.com/mrunalicodes/safeAI.git
cd safeAI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run SAFEAI

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Safety Note

SAFEAI provides informational safety guidance and may not always assess a situation correctly. In an immediate emergency in India, call 112. Do not rely on SAFEAI as a substitute for emergency services.

Keep API keys and other secrets private. Never commit them to GitHub.
