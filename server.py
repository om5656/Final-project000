from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Render home page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    """Process text input and return emotion analysis."""
    data = request.get_json()
    text = data.get('text', '').strip()

    result = emotion_detector(text)

    if result.get('dominant_emotion') is None:
        return jsonify({"message": "Invalid text! Please try again!"})

    output_str = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify({"result": output_str, "full_output": result})

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
