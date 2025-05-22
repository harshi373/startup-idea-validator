from flask import Flask, request, jsonify
import requests
from prompts import get_prompt
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HEADERS = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}
@app.route('/', methods=['GET'])
def home():
    return "Startup Validator Backend Running!"

@app.route("/validate", methods=["POST"])
def validate_idea():
    data = request.get_json()
    prompt = get_prompt(data["idea"])
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
    result = response.json()
    return jsonify({"result": result[0]["generated_text"] if isinstance(result, list) else result})

if __name__ == "__main__":
    app.run(debug=True)
