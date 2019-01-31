# tokenizing: work_tokenizing, sentence_tokenizing
# corpora: body of text
# lexicon: word and their means

from nltk.tokenize import sent_tokenize, word_tokenize

text = '''Hi, this is Prashant who loves doing code for Full-Stack Development. I've completed my graduation
            from Staffordshire University, my concentration was Software Engineering !!'''
print(word_tokenize(text))
print(sent_tokenize(text))
