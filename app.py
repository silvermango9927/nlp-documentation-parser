from flask import Flask, render_template, request
from qa_model import getAnswer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    question = request.form.get('question')
    # answer = getAnswer(question)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)