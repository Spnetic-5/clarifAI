from flask import Flask, render_template, url_for, request

from pprint import pprint
import simplejson as json
import sys 
from nltk.corpus import brown
from nltk.corpus import reuters
import nltk
from nltk.corpus import PlaintextCorpusReader
# from . import Suggestion 



app = Flask(__name__)

# ---------------------------

def get_trigram_freq(tokens):
	tgs = list(nltk.trigrams(tokens))

	a,b,c = list(zip(*tgs))
	bgs = list(zip(a,b))
	return nltk.ConditionalFreqDist(list(zip(bgs, c)))

def get_bigram_freq(tokens):
	bgs = list(nltk.bigrams(tokens))

	return nltk.ConditionalFreqDist(bgs)

def appendwithcheck ( preds, to_append):
	for pred in preds:
	    if pred[0] == to_append[0]:
	        return
	preds.append(to_append)


def incomplete_pred(words, n):
	all_succeeding = bgs_freq[(words[n-2])].most_common()
	#print (all_succeeding, file=sys.stderr)
	preds = []
	number=0
	for pred in all_succeeding:
	    if pred[0].startswith(words[n-1]):
	        appendwithcheck(preds, pred)
	        number+=1
	    if number==3:
	        return preds
	if len(preds)<3:
	    med=[]
	    for pred in all_succeeding:
	        med.append((pred[0], nltk.edit_distance(pred[0],words[n-1], transpositions=True)))
	    med.sort(key=lambda x:x[1])
	    index=0
	    while len(preds)<3:
	        print (index, len(med))
	        if index<len(med):
	            if med[index][1]>0:
	                appendwithcheck(preds, med[index])
	            index+=1
	        if index>=len(preds):
	            return preds


new_corpus = PlaintextCorpusReader('./','.*')
tokens = brown.words() + new_corpus.words('chat.txt')

bgs_freq = get_bigram_freq(tokens)
tgs_freq = get_trigram_freq(tokens)

# return preds


# ----------------------------


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/predict', methods=['GET','POST'])
def predict_page():
	if request.method == "POST":
		enter = request.form['text'].strip()
		print(enter)


	

	work = "pred"
	string = enter 
	words = string.split()
	n = len(words)
	if work == "pred":
		if n == 1:
			bgs = bgs_freq[(string)].most_common(5)
			b = []
			for i in bgs:
				b.append(i[0])
			# print(pred)
			print("bgs ->" , bgs)
		elif n>1:
            #print (tgs_freq[(words[n-2],words[n-1])].most_common(5),file=sys.stderr)
			tgs = tgs_freq[(words[n-2],words[n-1])].most_common(5)
			# print("tgs ->" , tgs)
			
			pred = []
			for i in tgs:
				pred.append(i[0])
			print(pred)

	else:
		inc = incomplete_pred(words, n)
		print("inc ->" , inc)

	if n == 1:
		p = b
	else:
		p = pred


	# return pred 

	return render_template("index.html", s= enter, t = p)


if __name__ == '__main__':
	app.run(debug=True)