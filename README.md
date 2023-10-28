# nlp
This is the brain of the project.It uses django at its backend and uses Django rest framework to provie an API for the project.So how it work is that, whenever a user sends a message ,the frontend gives a post request to the api which contains the message ,the API then analyses the message and return a JSON object containg how negative ,positive or neutral the message is , from this data ,the frontend is easily able to identify the sentiment of the messsage.
## Technicalities
For proccesing the language we used *vader's sentiment analyser* which is a lexicon and rule-based sentiment analysis tool designed for natural language processing (NLP) tasks.Apart from that we have used django's rest framework
