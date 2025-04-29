from flask import Flask, render_template, request, jsonify
from faq_bot import load_faq, get_answer

app = Flask(__name__)

# Load FAQ data once
questions, answers = load_faq()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chatbot_response():
    user_msg = request.json['message']
    response = get_answer(user_msg, questions, answers)
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(debug=True)
