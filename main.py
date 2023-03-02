import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():
    url = utext.get('1.0',"end").strip()
    article = Article(url)

    article.download()
    article.parse()
    article.nlp()

    title.config(state="normal")
    summary.config(state="normal")

    title.delete('1.0',"end")
    title.insert('1.0',article.title)

    summary.delete('1.0','end')
    summary.insert('1.0',article.summary)

    title.config(state="disabled")
    summary.config(state="disabled")

    # print(f'Title:{article.title}')
    # print(f'Summary:{article.summary}')


root = tk.Tk()
root.title("Article summary")

tlabel =tk.Label(root,text="Title")
tlabel.pack()

title = tk.Text(root,height=1,width=140)
title.config(state="disabled",bg='#dddddd')
title.pack()

slabel =tk.Label(root,text="Summary")
slabel.pack()

summary = tk.Text(root,height=20,width=140)
summary.config(state="disabled",bg='#dddddd')
summary.pack()


ulabel =tk.Label(root,text="URL")
ulabel.pack()

utext = tk.Text(root,height=1,width=140)
utext.pack()

btn = tk.Button(root,text="Summarize",command=summarize)
btn.pack()

root.geometry('1200x600')
root.mainloop()
