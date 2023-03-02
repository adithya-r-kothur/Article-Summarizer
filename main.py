import tkinter
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

url ='https://medium.com/@todbotts.triangles/what-is-good-bad-code-an-illustrated-example-for-non-programmers-1222b600a0f0'

article = Article(url)

article.download()
article.parse()
article.nlp()

print(f'Title:{article.title}')
print(f'Summary:{article.summary}')
