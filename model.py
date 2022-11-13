from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from transformers import pipeline
from scraper import get_html

# Init variables from scraper.py
url = 'https://scikit-learn.org/stable/modules/sgd.html'
context = get_html(url)

# Load model and tokenizer

model = AutoModelForQuestionAnswering.from_pretrained("deepset/tinyroberta-squad2")

question = str(input('What is your question: '))

tokenizer = AutoTokenizer.from_pretrained("deepset/tinyroberta-squad2")
tokenizer.encode(question, truncation=True, padding=True)

# Creating a pipeline for QA
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

print(nlp({
    'question': question,
    'context': context
}))
