import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    client = OpenAI(api_key=api_key)
else:
    client = None


@app.route("/")
def home():
    return render_template("index.html")


def local_analysis(situation):
    text = situation.lower()

    high_risk_words = [
        "attack", "attacking", "weapon", "gun", "knife",
        "kidnap", "kidnapping", "rape", "fire", "bleeding",
        "unconscious", "help me", "following me",
        "chasing me", "threatening", "danger"
    ]

    medium_risk_words = [
        "scared", "afraid", "stalking", "stalker",
        "alone", "unsafe", "suspicious", "threat",
        "harassment", "lost"
    ]

    if any(word in text for word in high_risk_words):
        risk = "HIGH"

        summary = "The situation may involve immediate danger."

        reason = (
            "The description contains signs that may indicate "
            "a potentially serious or immediate safety risk."
        )

        actions = [
            "Move to a safe and public place if possible.",
            "Contact local emergency services or a trusted person.",
            "Avoid confronting the threatening person if it could increase danger."
        ]

        avoid = [
            "Do not confront or provoke the person.",
            "Do not move to an isolated location."
        ]

        emergency = (
            "If you are in immediate danger, contact local emergency "
            "services and seek help from people nearby."
        )

    elif any(word in text for word in medium_risk_words):
        risk = "MEDIUM"

        summary = "The situation may involve a potential safety concern."

        reason = (
            "The description suggests that you may feel unsafe or "
            "that there may be a developing risk."
        )

        actions = [
            "Move toward a safe and populated area.",
            "Inform a trusted person about your situation.",
            "Keep your phone accessible and stay aware of your surroundings."
        ]

        avoid = [
            "Do not isolate yourself unnecessarily.",
            "Avoid confronting a suspicious person."
        ]

        emergency = (
            "If the situation becomes immediately dangerous, "
            "contact local emergency services."
        )

    else:
        risk = "LOW"

        summary = "No clear immediate danger was detected from the description."

        reason = (
            "The situation does not contain obvious indicators of "
            "an immediate emergency."
        )

        actions = [
            "Stay aware of your surroundings.",
            "Keep your phone accessible.",
            "Contact a trusted person if you begin to feel unsafe."
        ]

        avoid = [
            "Avoid ignoring a situation that becomes threatening.",
            "Avoid going somewhere isolated if you feel uncomfortable."
        ]

        emergency = (
            "If the situation changes or you feel in immediate danger, "
            "move to safety and contact emergency services."
        )

    return {
        "risk": risk,
        "summary": summary,
        "reason": reason,
        "actions": actions,
        "avoid": avoid,
        "emergency": emergency
    }


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Invalid request."
        }), 400

    situation = data.get("situation", "").strip()

    if not situation:
        return jsonify({
            "error": "Please describe your situation."
        }), 400

    prompt = f"""
You are SAFEAI, an emergency and personal safety assistant.

Analyze the user's situation and provide practical, calm and safety-focused guidance.

User situation:
{situation}

Return ONLY valid JSON in this exact format:

{{
    "risk": "LOW",
    "summary": "short summary of the user's situation",
    "reason": "short explanation",
    "actions": [
        "action 1",
        "action 2",
        "action 3"
    ],
    "avoid": [
        "thing to avoid 1",
        "thing to avoid 2"
    ],
    "emergency": "short emergency guidance"
}}

Risk must be exactly one of:
LOW, MEDIUM, HIGH

Important:
- If there is immediate danger, prioritize getting to a safe/public place and contacting local emergency services or a trusted person.
- Do not claim that you contacted emergency services.
- Do not provide dangerous instructions.
- Keep the advice practical and concise.
"""

    try:

        if client is None:
            raise Exception("OpenAI API key not configured.")

        response = client.responses.create(
            model="gpt-5.6-luna",
            input=prompt
        )

        result = response.output_text

        return jsonify({
            "result": result,
            "source": "AI"
        })

    except Exception as e:

        print("OpenAI unavailable. Using local SAFEAI analysis.")
        print("Error:", e)

        result = local_analysis(situation)

        return jsonify({
            "result": result,
            "source": "LOCAL"
        })


if __name__ == "__main__":
    app.run(debug=True)