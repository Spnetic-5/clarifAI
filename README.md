# clarifAI
The Real-time assisted writing system provides the ability to autocomplete words and suggests predictions for the next word. This makes typing faster, more intelligent and reduces effort. It is a Natural Language Processing concerned with predicting the text given the precceding text. It can be used as an web application.

# Methodology
Assistant system provides the ability to autocomplete words and suggests predictions for the next word. This makes typing faster, more intelligent and reduces effort. The implementation involves using a large corpus.
The initial task will be to design a keyboard interface as a web app. The keyboard layout consists of all keys which are present on a physical keyboard. The keyboard's interface will show the top three predictions for a given word sequence and suggest word-completion.
This interface will be achieved by designing in HTML, CSS and JavaScript. 
If space key is not pressed, then the server returns the auto-completions/spelling correction possible for the given word by using which of the word predictions previously made starts with the what the user is typing. If less than three such matches are found, the minimum edit distance module takes over and returns the remaining predictions, to make a total of three predictions at all times.
These predictions are converted to JSON and sent to the keyboard module.
The keyboard unwraps the JSON and puts the predictions over the keys.
![image](https://user-images.githubusercontent.com/64076774/112019984-fd1dc600-8b55-11eb-93ee-e363edc155da.png)

Models Considered for word prediction:
**N-grams Model**
Probabilistic models are used for computing the probability of an entire sentence or for giving a probabilistic prediction of what the next word will be in a sequence. 
This model involves looking at the conditional probability of a word given the previous words.If we consider each word occurring in its correct location as an independent event. We might represent this probability as:
![image](https://user-images.githubusercontent.com/64076774/112020610-7f0def00-8b56-11eb-9dc2-9611fdb84b4a.png)


**LSTM Model:**
Long Short-Term Memory (LSTM) networks are a type of recurrent neural network capable of learning order dependence in sequence prediction problems.
LSTM (Long Short-Term Memory) are very good for analyzing sequences of values and predicting the next one. 
LSTM model uses Deep learning with a network of artificial “cells” that manage memory, making them better suited for text prediction than traditional neural networks and other models.
LSTM have the ability to remove or add information to cell state regulated by structures called gates.

![LSTMcell](https://user-images.githubusercontent.com/64076774/112019391-65b87300-8b55-11eb-830c-226277acbca0.png)

Advantage: Standard RNNs and other language models become less accurate when the gap between the context and the word to be predicted increases. Here’s when LSTM comes in use to tackle the long-term dependency problem because it has memory cells to remember the previous context.
**Future Scope:**
We could add an autocorrect feature like Grammarly.
Try to improve our LSTM model to maximize the results for the word /phrase prediction.
We could also implement an app where one can write an application letter and the app will predict the next appropriate words according to the subject of the letter.  


 
 ### DATASETS
 * https://www.kaggle.com/thanatoz/hinglish-blogs?select=data_119.txt

 * https://www.gutenberg.org/cache/epub/5200/pg5200.txt
  
#### [Recurrent Neural Networks | Sequence Models | Natural Language Processing](https://www.youtube.com/playlist?list=PL1w8k37X_6L_s4ncq-swTBvKDWnRSrinI) 

#### [A Guide to Coding Placements by Shreyansh Chheda](https://dscvjti.medium.com/how-to-start-coding-the-right-way-b30131c4dd4a)


