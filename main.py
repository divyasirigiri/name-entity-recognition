from logging import debug
from flask import Flask, render_template, request
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

app1 = Flask(__name__)


@app1.route('/')
def hello():
    return render_template('base.html')

@app1.route('/define',methods = ['POST'])
def define():
    new=[]
    new1=[]
    ip_word = request.form.get('ip-word')
    ip2 = request.form.get('ip2')
    if ip2=="Verbs":
        words = nltk.word_tokenize(ip_word)
        pos_tag = nltk.pos_tag(words)
        for i in pos_tag:
            if i[1]== "VB" or i[1]=="VBG" or i[1] == "VBD" or i[1] == "VBN" or i[1]=="VBP" or i[1]=="VBZ":
                new.append(i[0])
        res = new
    elif ip2=="NER":
        words = nltk.word_tokenize(ip_word)
        pos_tag = nltk.pos_tag(words)
        named_entity = nltk.ne_chunk(pos_tag)
        res = named_entity
    elif ip2=="Root Form":
        try:

            lemma = WordNetLemmatizer()
            punct = string.punctuation
            stop_words = stopwords.words('english')
            for word in nltk.word_tokenize(ip_word):
                if word not in punct:
                    if word not in stop_words:
                        new1.append(lemma.lemmatize(word , 'v'))                 
            res= " ".join(new1)
        except:
            res=ip_word 
    

    return render_template('base.html',translated_text=f'\n the {(ip2)} in the text "{(ip_word)}"  is/are :  {res}')

if __name__=='__main__':
    app1.run(debug=True)
