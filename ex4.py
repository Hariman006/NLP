from nltk.stem import PorterStemmer
ps=PorterStemmer()
sentence = input("Enter a sentence: ")
words = sentence.split()
for w in words:
    print("Word:",ps.stem(w))
