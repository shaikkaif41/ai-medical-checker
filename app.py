from flask import Flask, render_template, request
from services.llm import analyze_symptoms

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    # Collect patient details
    patient = {
        "name": request.form.get("name"),
        "age": request.form.get("age"),
        "gender": request.form.get("gender"),
        "height": request.form.get("height"),
        "weight": request.form.get("weight"),
        "symptoms": request.form.get("symptoms"),
        "duration": request.form.get("duration"),
        "temperature": request.form.get("temperature")
    }

    # Basic Validation
    if (
        not patient["name"]
        or not patient["age"]
        or not patient["gender"]
        or not patient["symptoms"]
    ):
        return "Please fill all required fields."

    try:
        # Call Gemini AI
        result = analyze_symptoms(patient)

    except Exception as e:
        result = f"Error while generating medical analysis:\n\n{str(e)}"

    return render_template(
        "result.html",
        patient=patient,
        result=result
    )


@app.route("/about")
def about():
    return """
    <h2>AI Medical Symptom Checker</h2>

    <p>
    This project uses Google's Gemini AI to analyze symptoms
    and provide educational information.
    </p>

    <p>
    It is NOT intended to diagnose diseases or replace
    professional medical advice.
    </p>
    """


@app.route("/health")
def health():
    return {
        "status": "running",
        "application": "AI Medical Symptom Checker"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )