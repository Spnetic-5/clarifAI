# clarifAI
The Real-time assisted writing system provides the ability to suggest predictions for the next word to type. This makes typing faster, more intelligent and reduces effort. It is a Natural Language Processing concerned with predicting the text given the precceding text. It can be used as an web application.

# 📝 Methodology
Assistant system provides the ability to autocomplete words and suggests predictions for the next word. This makes typing faster, more intelligent and reduces effort. The implementation involves using a large corpus.
The initial task will be to design a keyboard interface as a web app. The keyboard layout consists of all keys which are present on a physical keyboard. The keyboard's interface will show the top three predictions for a given word sequence and suggest word-completion.
This interface will be achieved by designing in HTML, CSS and JavaScript. 
If space key is not pressed, then the server returns the auto-completions/spelling correction possible for the given word by using which of the word predictions previously made starts with the what the user is typing. If less than three such matches are found, the minimum edit distance module takes over and returns the remaining predictions, to make a total of three predictions at all times.
These predictions are converted to JSON and sent to the keyboard module.
The keyboard unwraps the JSON and puts the predictions over the keys.
![image](https://user-images.githubusercontent.com/64076774/112019984-fd1dc600-8b55-11eb-93ee-e363edc155da.png)

Models Considered for word prediction:

* **N-grams Model:**
Probabilistic models are used for computing the probability of an entire sentence or for giving a probabilistic prediction of what the next word will be in a sequence. 
This model involves looking at the conditional probability of a word given the previous words.If we consider each word occurring in its correct location as an independent event. We might represent this probability as:

<p align="center" >
<img src="https://user-images.githubusercontent.com/64076774/112020610-7f0def00-8b56-11eb-9dc2-9611fdb84b4a.png"> <br>
We can use the chain rule of probability to decompose this probability:<br>
 <img  src="https://user-images.githubusercontent.com/66636289/119120334-ca0a8c80-ba49-11eb-90dc-e3ca26b39853.png"><br>
Minimum Edit Distance:<br>
<img align="center" src="https://user-images.githubusercontent.com/66636289/119120091-8152d380-ba49-11eb-9fe9-3bb0e9a87f6c.png"><br>
</p>


* **LSTM Model:**
Long Short-Term Memory (LSTM) networks are a type of recurrent neural network capable of learning order dependence in sequence prediction problems.
LSTM (Long Short-Term Memory) are very good for analyzing sequences of values and predicting the next one. 
LSTM model uses Deep learning with a network of artificial “cells” that manage memory, making them better suited for text prediction than traditional neural networks and other models.
LSTM have the ability to remove or add information to cell state regulated by structures called gates.<br>

<p align="center" >
<img height="300" width="400" src="https://user-images.githubusercontent.com/66636289/116988049-767c0d00-aced-11eb-98f0-6e68cb23d514.png">
</p>

Advantage: Standard RNNs and other language models become less accurate when the gap between the context and the word to be predicted increases. Here’s when LSTM comes in use to tackle the long-term dependency problem because it has memory cells to remember the previous context.

## 🤖 Technology Stack:
* Front-end - HTML, CSS, JS
* Back-end -  [Flask](https://flask.palletsprojects.com/en/1.1.x/), Python
* Models - [N-grams](https://en.wikipedia.org/wiki/N-gram), [LSTM](https://en.wikipedia.org/wiki/Long_short-term_memory)
* Frameworks - Keras, Tensorflow
* Libraries - nltk, numpy

## 🛠️ Project Setup
```
$ git clone https://github.com/Spnetic-5/clarifAI.git
```
```
$ python app.py 
```


## 🖼 Working Example:
 * Hindi:
 
 ![image](https://user-images.githubusercontent.com/66636289/116987344-90692000-acec-11eb-94d7-962d0a633ed0.png)

 * English:

 ![image](https://user-images.githubusercontent.com/66636289/116987532-cdcdad80-acec-11eb-82d8-525fa229a40a.png)

### DATASETS Used:
 * https://www.kaggle.com/thanatoz/hinglish-blogs?select=data_119.txt

 * https://www.gutenberg.org/cache/epub/5200/pg5200.txt

### ⚡ Applications:
 * This project predicts the next possible word based on the input provided by the user. This project supports English as well as Hindi language.

## 🔮 Future Scope:
* We could add an autocorrect feature like Grammarly.
* Try to improve our LSTM model to maximize the results for the word /phrase prediction.
* We could also implement an app where one can write an application letter and the app will predict the next appropriate words according to the subject of the letter.  

### 👩‍💻 Contributors:
 * [Saurabh Suresh Powar](https://github.com/Spnetic-5)
 * [Sakshi Chikshe](https://github.com/Sakshi-0311)
 * [Rutuja Kolte](https://github.com/Rutuja-Kolte)
 * [Khushi Barjatia](https://github.com/khushibarjatia)

 ### 👨‍🏫 Mentor:
 * [Shreyansh Chheda](https://github.com/shrey-c)
 
#### 🔗 Acknowledgements:
   * [Deep Learning Specialization Andrew NG](https://www.coursera.org/specializations/deep-learning?network=g&utm_source=gg&creativeid=506864295332&matchtype=b&adgroupid=120914521673&gclid=Cj0KCQjw4cOEBhDMARIsAA3XDRjA38BsZVS0VgzvKEwDHtfavwsFIQcoqs5dPq9-wKM518-Va9-L9XMaAnZwEALw_wcB&keyword=&utm_content=94-BrandedSearch-IN&hide_mobile_promo=&utm_campaign=94-BrandedSearch-IN&campaignid=1776545273&devicemodel=&adpostion=&utm_medium=sem&device=c)
   * [Recurrent Neural Networks | Sequence Models | Natural Language Processing](https://www.youtube.com/playlist?list=PL1w8k37X_6L_s4ncq-swTBvKDWnRSrinI) 
   * [COC-VJTI](https://www.communityofcoders.in/) 
