
from flask import Flask, request, jsonify
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)

# Example route for sentiment analysis
@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get("text", "")
    sentiment = "positive" if "good" in text else "negative"  # Simple sentiment analysis example
    return jsonify({"sentiment": sentiment})

# Example route for emotion detection
@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    data = request.files['image']
    img = Image.open(data)
    img = np.array(img)
    emotion = "happy"  # Placeholder for actual emotion model inference
    return jsonify({"emotion": emotion})

if __name__ == '__main__':
    app.run(debug=True)
