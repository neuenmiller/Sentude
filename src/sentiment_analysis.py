from textblob import TextBlob
import nltk
nltk.download('punkt')

import os


def analyze_sentiment_sentence_level(text):
    blob = TextBlob(text)
    sentence_sentiments = []
    max_polarity = 0
    total_polarity = 0
    num_sentences = len(blob.sentences)
    
    for sentence in blob.sentences:
        analysis = TextBlob(str(sentence))
        polarity = analysis.sentiment.polarity
        max_polarity += abs(polarity)
        total_polarity += polarity

        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        sentence_sentiments.append((str(sentence), sentiment, polarity))
        
    return sentence_sentiments, max_polarity, total_polarity, num_sentences
        
    
def read_file_and_analyze(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return analyze_sentiment_sentence_level(text)


filename = 'src/ID2.txt'

sentence_sentiments, max_polarity, total_polarity, num_sentences = read_file_and_analyze(filename)
# print(f"Sentence Sentiments: {sentence_sentiments}")
print(f"Max Polarity: {max_polarity}")
print(f"Total Polarity: {total_polarity}")
print(f"Average Polarity: {total_polarity/num_sentences}")
print(f"Number of Sentences: {num_sentences}, therefore maxium of {num_sentences} sentiments")