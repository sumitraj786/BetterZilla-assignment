from flask import Flask, render_template, request
from chatbot import ask_chatbot_personalized

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    user_info = request.form['user_info']
    response = ask_chatbot_personalized(question, user_info)
    return render_template('index.html', question=question, response=response)

if __name__ == "__main__":
    app.run(debug=True)
