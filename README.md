# SAFEAI – AI Emergency & Safety Assistant

SAFEAI is an AI-powered emergency and safety assistant designed to help users analyze dangerous situations and provide appropriate safety guidance.

## Features

- 🛡️ Analyze emergency situations
- 🚨 Classify situations as LOW, MEDIUM, or HIGH risk
- 🤖 AI-powered safety recommendations
- ⚡ Simple and user-friendly interface
- 🔒 Designed with safety as the priority

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

Open `http://127.0.0.1:5000` in your browser.

### Note
Some AI features may require a valid API key configured locally. Never commit API keys, passwords, or other secrets to GitHub.
