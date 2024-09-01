from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    dest_language = data.get('dest_lang')
    
    if not text or not dest_language:
        return jsonify({"error": "Missing text or destination language"}), 400
    
    try:
        translated = translator.translate(text, dest=dest_language)
        return jsonify({"translated_text": translated.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)