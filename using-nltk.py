# Printing Hello World using nltk
import nltk

sentence = "This is a sentence containing Hello World"
target_words = nltk.word_tokenize(sentence)[-2:]

print(' '.join(target_words))
