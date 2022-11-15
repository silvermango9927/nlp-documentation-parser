from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from transformers import pipeline
from scraper import get_html

# Init variables from scraper.py
def getAnswer(question):
    context = get_html()

    # Load model and tokenizer

    model = AutoModelForQuestionAnswering.from_pretrained("deepset/tinyroberta-squad2")

    tokenizer = AutoTokenizer.from_pretrained("deepset/tinyroberta-squad2")
    tokenizer.encode(question, truncation=True, padding=True)

    # Creating a pipeline for QA
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

    return (nlp({
        'question': question,
        'context': context
    }))