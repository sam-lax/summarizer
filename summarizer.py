from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter


stop_words = set(stopwords.words('english'))


paragraph = input('Text: ')
sentences = paragraph.split('.')


word_tokens = []
for sentence in sentences:
    word_tokens.append(word_tokenize(sentence))

filtered_word_tokens = []
for sentence in word_tokens:
    if sentence != []:
        filtered_word_tokens.append([w.lower() for w in sentence if not w in stop_words and w != ',' and w != '.' and len(w) > 2])
filtered_word_tokens = [[word_token for word_token in arr if not word_token in stop_words] for arr in filtered_word_tokens]


counted = Counter()
for sentence in filtered_word_tokens:
    counted += Counter(sentence)


freqs = []
for i in range(len(counted)):
    freqs.append(counted.most_common()[i][1])
weights = [num / freqs[0] for num in freqs]


sums = []
for i in range(len(filtered_word_tokens)):
    sums.append(sum(weights[:len(filtered_word_tokens[i])]))
    del weights[:len(filtered_word_tokens[i])]


output = ''
i = 0
while sums != [0] * len(sums):
    index = sums.index(max(sums))
    for words in filtered_word_tokens[index]:
        output += words + ' '
    output += '\n'
    sums[index] = 0

if __name__ == '__main__':
    print('\nSummary: \n' + str(output))