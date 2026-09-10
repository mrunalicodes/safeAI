from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    situation = data.get("situation", "").strip()

    if not situation:
        return jsonify({"error": "Please describe your situation."}), 400

    prompt = f"""
You are SAFEAI, an emergency and personal safety assistant.

Analyze the user's situation and provide practical, calm and safety-focused guidance.

User situation:
{situation}

Return ONLY valid JSON in this exact format:

{{
    "risk": "LOW",
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
        response = client.responses.create(
            model="gpt-5.6-luna",
            input=prompt
        )

        result = response.output_text

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)