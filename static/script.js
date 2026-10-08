async function analyzeSituation() {
    const situation = document.getElementById("situation").value.trim();
    const result = document.getElementById("result");

    if (situation === "") {
        alert("Please describe your situation first.");
        return;
    }

    result.innerHTML = "<p>🤖 SAFEAI is analyzing...</p>";

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                situation: situation
            })
        });

        const data = await response.json();

        if (data.error) {
            result.innerHTML = `<p>❌ ${data.error}</p>`;
            return;
        }

        const aiResult =
            typeof data.result === "string"
                ? JSON.parse(data.result)
                : data.result;

        const summary =
            aiResult.summary ||
            aiResult.reason ||
            "No summary available.";

        const riskClass =
            aiResult.risk.trim().toLowerCase();

        result.innerHTML = `
            <div class="result-card ${riskClass}">

                <h2>🚨 ${aiResult.risk} RISK</h2>

                <h3>📋 Incident Summary</h3>
                <p>${summary}</p>

                <h3>Why?</h3>
                <p>${aiResult.reason}</p>

                <h3>⚠️ Immediate Actions</h3>
                <ul>
                    ${aiResult.actions
                        .map(action => `<li>${action}</li>`)
                        .join("")}
                </ul>

                <h3>🚫 Avoid</h3>
                <ul>
                    ${aiResult.avoid
                        .map(item => `<li>${item}</li>`)
                        .join("")}
                </ul>

                <h3>📞 Emergency Guidance</h3>
                <p>${aiResult.emergency}</p>

            </div>
        `;

    } catch (error) {

        result.innerHTML =
            "<p>❌ Something went wrong. Please try again.</p>";

        console.error(error);
    }
}


function triggerSOS() {

    const contactNumber =
        document.getElementById("contactNumber").value.trim();

    let locationLink = "Location not available.";

    if (window.currentLocation) {

        const { latitude, longitude } =
            window.currentLocation;

        locationLink =
            `https://www.google.com/maps?q=${latitude},${longitude}`;
    }

    const choice = confirm(
        "🚨 EMERGENCY SOS\n\n" +
        "If you are in immediate danger, call emergency services (112).\n\n" +
        "Click OK to continue to emergency call options."
    );

    if (!choice) {
        return;
    }

    const emergencyMessage =
        "🚨 EMERGENCY ALERT\n\n" +
        "I may be in danger. Please contact me immediately.\n\n" +
        "📍 Location:\n" +
        locationLink;

    const action = confirm(
        "🚨 Emergency Options\n\n" +
        "OK = Call 112\n" +
        "Cancel = Prepare emergency message"
    );

    if (action) {

        window.location.href = "tel:112";

    } else {

        window.emergencyMessage = emergencyMessage;

        alert(
            "📋 Emergency message prepared!\n\n" +
            "You can use the Trusted Contact section to copy and share it."
        );
    }
}function startVoiceInput() {
    const situation = document.getElementById("situation");

    const SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        alert("❌ Voice input is not supported in this browser.");
        return;
    }

    const recognition = new SpeechRecognition();

    recognition.lang = "en-IN";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.start();

    recognition.onstart = function() {
        alert("🎤 Listening... Please speak your situation.");
    };

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        situation.value = transcript;
    };

    recognition.onerror = function(event) {
        alert("❌ Voice input error: " + event.error);
    };
}
function sendEmergencyMessage() {

    const name = document.getElementById("contactName").value.trim();
    const number = document.getElementById("contactNumber").value.trim();
    const situation = document.getElementById("situation").value.trim();

    const resultCard = document.querySelector(".result-card");

    let risk = "UNKNOWN";
    let summary = "No AI analysis available.";

    if (resultCard) {

        const riskHeading = resultCard.querySelector("h2");
        const paragraphs = resultCard.querySelectorAll("p");

        if (riskHeading) {
            risk = riskHeading.innerText
                .replace("🚨 ", "")
                .replace(" RISK", "");
        }

        if (paragraphs.length > 0) {
            summary = paragraphs[0].innerText;
        }
    }

    let locationText = "Location not shared.";

    if (window.currentLocation) {

        const { latitude, longitude } = window.currentLocation;

        locationText =
            `https://www.google.com/maps?q=${latitude},${longitude}`;
    }

    if (name === "" || number === "") {
        alert("Please enter trusted contact name and phone number.");
        return;
    }

    const message = `🚨 EMERGENCY ALERT

Hi ${name},

I may be in an unsafe situation.

Risk Level: ${risk}

Incident Summary:
${summary}

My Situation:
${situation}

Location:
${locationText}

Please contact me immediately and check on me.`;

    const messageBox =
        document.getElementById("contactMessage");

    messageBox.innerHTML = `
        <div class="message-box">
            <h3>📩 Emergency Message Ready</h3>

            <p>${message.replace(/\n/g, "<br>")}</p>

            <button onclick="copyEmergencyMessage()">
                📋 Copy Message
            </button>
        </div>
    `;

    window.emergencyMessage = message;
}


function copyEmergencyMessage() {

    navigator.clipboard.writeText(
        window.emergencyMessage
    );

    alert("Emergency message copied!");
}


function getLocation() {

    const locationResult =
        document.getElementById("locationResult");

    if (!navigator.geolocation) {

        locationResult.innerHTML =
            "<p>❌ Location is not supported by this browser.</p>";

        return;
    }

    locationResult.innerHTML =
        "<p>📍 Getting your location...</p>";

    navigator.geolocation.getCurrentPosition(

        function(position) {

            const latitude =
                position.coords.latitude;

            const longitude =
                position.coords.longitude;

            window.currentLocation = {
                latitude: latitude,
                longitude: longitude
            };

            const mapsLink =
                `https://www.google.com/maps?q=${latitude},${longitude}`;

            locationResult.innerHTML = `
                <div class="location-box">

                    <p>✅ Location found!</p>

                    <p>
                        📍 Latitude:
                        ${latitude.toFixed(5)}
                    </p>

                    <p>
                        📍 Longitude:
                        ${longitude.toFixed(5)}
                    </p>

                    <a href="${mapsLink}" target="_blank">
                        🗺️ Open Location in Google Maps
                    </a>

                </div>
            `;
        },

        function(error) {

            locationResult.innerHTML =
                "<p>❌ Unable to get your location. Please allow location access.</p>";

            console.error(error);
        }
    );
}