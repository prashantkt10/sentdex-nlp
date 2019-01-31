# removing stop words


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# print(stopwords.words('english'))

example_sent = '''India needs focus on development rather than communalism, politicians must rather focus on
                    development rather than meaningless issues !!! The future of India is in hands of 
                    politicians only.'''
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sent)
filtered_sentence = [w for w in words if w not in stop_words]

print(example_sent)
print(filtered_sentence)
