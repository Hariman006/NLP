from nltk import ngrams
sentence = "Game running: generating n-grams"
n = 2  
print("Input Sentence:")
print(sentence)
print("\nValue of n:", n)
print("\nWord n-grams:")
words = sentence.split()
word_ngrams = ngrams(words, n)
for gram in word_ngrams:
    print(gram)
print("\nCharacter n-grams:")
char_ngrams = ngrams(sentence, n)
for gram in char_ngrams:
    print("".join(gram))
