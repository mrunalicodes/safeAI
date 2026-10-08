# 🛡️ SAFEAI — AI-Powered Safety Assistant

SAFEAI is an AI-powered emergency and personal safety assistant designed to provide quick, practical and safety-focused guidance when a user feels unsafe.

## 🚀 Features

- 🤖 AI-powered situation analysis
- 🚦 LOW / MEDIUM / HIGH risk detection
- 📋 AI-generated incident summary
- ⚡ Immediate safety actions
- 🚫 Things to avoid
- 📞 Emergency guidance
- 🎤 Voice-based situation input
- 📍 Current location detection
- 🗺️ Google Maps location link
- 📱 Trusted contact emergency message
- 📋 Copy emergency message
- 🚨 Emergency SOS interface
- 🆘 Local safety analysis fallback when AI is unavailable

## 🛠️ Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript
- OpenAI API
- Browser Geolocation API
- Web Speech API
- Google Maps

## 🔄 How It Works

1. User describes their situation.
2. SAFEAI sends the situation to the Flask backend.
3. The AI analyzes the situation.
4. SAFEAI generates a risk level and safety guidance.
5. The user can view recommended safety actions.
6. The user can optionally get their location.
7. The user can prepare an emergency message for a trusted contact.

## 📂 Project Structure

```text
safeAI/
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── start_safeai.bat