
import nltk
import re
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import glob
import os

file_list = glob.glob(os.path.join(os.getcwd(), "C:/folder1/folder2/Clean_ABBV", "*.txt"))

corpus = []

for file_path in file_list:
    with open(file_path) as f_input:
        corpus.append(f_input.read())



import ref_data as rf
dictionary = rf.get_sentiment_word_dict()
negative_words = dictionary['Negative']
positive_words = dictionary['Positive']
negative_list=[]
positive_list = []

for i in corpus:
    tokenised= word_tokenize(i)
    for word in tokenised:
        if word in negative_words:
            negative_list.append(word)
        if word in positive_words:
            positive_list.append(word)

negative_document = ' '.join(negative_list)
positive_document = ' '.join(positive_list)


wc = WordCloud(background_color='white',width=1800, height=1000, min_font_size=10,colormap='Reds',relative_scaling=0.0001, collocations=False).generate(negative_document)
fig, ax = plt.subplots(figsize=(8,6))
ax.imshow(wc)
ax.set_axis_off()
plt.savefig('ABBVnegativeswordcloud.png')


wc = WordCloud(background_color='white',width=1800, height=1000, min_font_size=10,colormap='Greens',relative_scaling=0.00001, collocations=False).generate(positive_document)
fig, ax = plt.subplots(figsize=(8,6))
ax.imshow(wc)
ax.set_axis_off()
plt.savefig('ABBVpositivewordcloud.png')