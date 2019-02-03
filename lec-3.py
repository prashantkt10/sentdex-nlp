from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "Pythonner", "pythoning", "pythonned", "pythonly"]
# words = word_tokenize(example_words)
# print(words)

for w in example_words:
    print(ps.stem(w))

example_sent = "Programers program with programing languages"
example_sent = word_tokenize(example_sent)
# print(example_sent)
for w in example_sent:
    print(ps.stem(w))
