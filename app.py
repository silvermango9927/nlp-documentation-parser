from flask import Flask, render_template, request
from qa_model import getAnswer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
        question = request.args.get('question')
        answer = getAnswer(question)
        return render_template('index.html', answer=answer['answer'])

if __name__ == '__main__':
    app.run(debug=True)