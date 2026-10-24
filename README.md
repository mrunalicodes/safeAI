
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

## Screenshots

### Home Page
![SAFEAI Home Page](Screenshot%202026-10-24%20181401.png)

### AI Assistant
![SAFEAI AI Assistant](Screenshot%202026-10-24%20181440.png)

### Location Feature
![SAFEAI Location](Screenshot%202026-10-24%20181519.png)

## Testing

The following features have been tested successfully:

- Situation analysis and risk classification
- Voice input
- Location sharing with Google Maps
- Emergency message generation
- Copy emergency message
- SOS options

## Future Improvements

- Improve AI response reliability and error handling
- Add automated tests for core features
- Improve mobile responsiveness and accessibility
- Add secure user settings and trusted-contact management

## Disclaimer

SAFEAI is a safety-support tool, not a replacement for emergency services. AI-generated guidance may be inaccurate. In an immediate emergency in India, call 112.
## Running Tests

SAFEAI includes automated tests for its Flask routes and local risk analysis.

Install pytest:

```bash
pip install pytest
```

Run the test suite from the project directory:

```bash
python -m pytest -v
```

The tests cover:

- Home page response
- Invalid requests to the analysis endpoint
- Empty situation validation
- HIGH, MEDIUM, and LOW risk classification

The test suite can run without an OpenAI API key because it tests the local analysis function directly.
