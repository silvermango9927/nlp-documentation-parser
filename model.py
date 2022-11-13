from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from transformers import pipeline
from scraper import get_html

url = 'https://scikit-learn.org/stable/modules/sgd.html'
context = get_html(url)

model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")

question = 'What is the shape of the X array?'

tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
tokenizer.encode(question, truncation=True, padding=True)

nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

print(nlp({
    'question': question,
    'context': context
}))
