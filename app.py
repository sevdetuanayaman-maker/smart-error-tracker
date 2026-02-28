from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_errors():
    try:
        with open("errors.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_errors(errors):
    with open("errors.json", "w") as f:
        json.dump(errors, f)

@app.route("/add_error", methods=["POST"])
def add_error():
    data = request.json
    error = data.get("error")

    errors = load_errors()
    errors.append(error)

    save_errors(errors)

    return jsonify({"message": "Error saved"})

@app.route("/errors", methods=["GET"])
def get_errors():
    return jsonify(load_errors())

if __name__ == "__main__":
    app.run(debug=True)
    