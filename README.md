# random-test
This tool can be used to generate a random test based on questions from a database. To implement ths functionality, MongoDB was used.

# Requirements
This app builds upon a MongoDB database. If you want to use it for your purposes, you need to have Mongo installed. Once you have your server set up, you need to pass the connection information like database name and the collection name on app startup.

# Features
* Two types of questions supported: 
    - Open Question
    - Closed Question (ABCD-like) with any number of answers.

* As far as closed questions are concerned, the answers to them are shuffled, so that two instances of the same test will most likely have them placed in different order.

* Add / Delete question straight from the app

* Generate a random test from the questions in the database. You need to specify the number of open and closed questions, and the randomizer will do the rest for you. You will never have to bother about cheating anymore!
