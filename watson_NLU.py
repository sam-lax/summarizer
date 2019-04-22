import json
from ibm_watson import NaturalLanguageUnderstandingV1 as NLU
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
import textract


file = 'report.txt'
#file = 'summary.docx'
#extension = 'docx'


def process_text(file, extension=None):
    if not extension:
        text = textract.process(file)
    else:
        text = textract.process(file, extension=extension)
    return text.decode()


def chunk(text):
    chunk_counts = []
    
    for i in range(1, int(len(text) / 50000) + 1):
        chunk_counts.append(i * 50000)
    chunk_counts.append(chunk_counts[-1] + len(text) % 50000)

    chunks = []
    while True:
        try:
            while i in range(len(chunk_counts)):
                chunks.append(text[chunk_counts[i]:chunk_counts[i+1]])
                i += 1
        except IndexError:
            break
    
    return chunks


def relevancy_dict(chunk):
    service = NLU(version='2018-03-16', url='https://gateway.watsonplatform.net/natural-language-understanding/api', iam_apikey='mOIwpTciIXb5WLmD3vp2Eo5LUsKuXIc_q_0ynDvTyHXs')
    response = service.analyze(text=chunk, features=Features(entities=EntitiesOptions(), keywords=KeywordsOptions())).get_result()
    analysis = json.dumps(response, indent=2)
    return json.loads(analysis)


# keywords = []; entities = [];
# 

