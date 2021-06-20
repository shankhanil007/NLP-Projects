import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """There are times when the night sky glows with bands of color. The bands may
begin as cloud shapes and then spread into a great arc across the entire sky. They
may fall in folds like a curtain drawn across the heavens. The lights usually grow
brighter, then suddenly dim. During this time the sky glows with pale yellow, pink,
green, violet, blue, and red. These lights are called the Aurora Borealis. Some
people call them the Northern Lights. Scientists have been watching them for
hundreds of years. They are not quite sure what causes them. In ancient times people were afraid of the Lights. They imagined that they saw fiery dragons in the
sky. Some even concluded that the heavens were on fire. """


stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
tokens = [token.text for token in doc]

punctuation = punctuation + '\n'

word_frequencies = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
                


max_frequency = max(word_frequencies.values())
max_frequency

for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency



sentence_tokens = [sent for sent in doc.sents]


sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]
                
select_length = int(len(sentence_tokens)*0.3)
select_length

summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
summary

final_summary = [word.text for word in summary]
summary = ' '.join(final_summary)

print(summary)
print(len(summary))