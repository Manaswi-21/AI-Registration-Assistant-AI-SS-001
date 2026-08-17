from flask import Flask, render_template, request, jsonify
from chatbot import RegistrationAssistant

app = Flask(__name__)
assistant = RegistrationAssistant()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"response": "Please enter a message.", "entities": {}})

    response, entities = assistant.get_response(message)
    return jsonify({"response": response, "entities": entities})

if __name__ == "__main__":
    app.run(debug=True)
