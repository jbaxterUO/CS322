# UOCIS322 - Project 3 #

You'll learn about JQuery and asynchronous requests in this project.

## Overview

The program is a simple anagram game designed for English-learning students in elementary and middle school. It presents a list of words to students and an anagram. The anagram is a jumble of some of the words, which are randomly chosen. Students attempt to type words that can be created from the jumble. When a matching word is typed, it is added to a list of solved words.

The vocabulary word list is fixed for one invocation of the server, so multiple students connected to the same server will see the same vocabulary list but may have different anagrams.

## Getting started

`flask_vocab.py` runs the anagram game, with the template `vocab.html`. This example uses a conventional interaction through a form, interacting only when the user submits the form. The vocabulary and anagram are currently loaded using basic JINJA. What you're supposed to do is to change the form interaction into an AJAX interaction (using JQuery).

## Updated Section 
Last updated by: Jesse Baxter
Email: jbaxter@uoregon.edu

## Project Overview
- The purpose of this project was to implement a simple anagram game. The game picks random words and create a jumble of letters that can be used to spell the randomly selected words. There is a list of all possible words when attempting to guess which words the jumble can create.

-The guesses are checked on each keystroke and a responsive message is displayed after each check. Each sucessful guess is stored in list below the input form box. After the required number of words are found the game redirects to a success page where you can elect to play again.


## Project Innerworkings
- The project uses flask from Python as a backend to handle the logic of the game. Flask also manages sessions for the project so the game can be played without having to redirect or send large amounts of information in the header each request. 

- The front end is handled by AJAX with jQuery to integrate the backend and frontend. 

- The file that the random words are pulled from is in the `vocab/data` directory and can be added to if the user would like to adjust the given words.

## Using The Project/Project Setup Options
- You need to have docker installed and you need to know how to navigate to your localhost or 
`127.0.0.1:YOURPORT[Default = 5000]` in the brower as prerequistes for using this project.

- The first step is to clone the repo. There are several things that can after the repo has been cloned. You generally only want to be in the `vocab` directory because that is where most adjustable options are and it is where you need to be when you call `docker build`. 

- Firstly you want to copy the credentials-skel.ini file in the `/project-3` directory to make your own credentials file and make sure it ends up in the `/vocab` directory. You can do this in one command `cp credentials-skel.ini vocab/credentials.ini`.

- After that you should generate a `secret key`, info here http://flask.pocoo.org/docs/0.12/quickstart/#sessions, and paste it into your credentials file as the `secret_key` value. 

- If you want to have a fixed seed to get the same results then set a `SEED` here as well, but by default it will be random each time.

- You can change the number of words needed to win here by updating the `sucess_at_here` variable.

- This is also where you can change the name of the file the words are pulled form. First you would want to add the file to `vocab/data` then change the name of the path in the `vocab` variable at the bottom of the credentials file to match. 

- Once the options are configured how you would like you should make sure you are in the `vocab` directory and then call `docker build -t NAMEYOULIKE .`, the -t tag and name are optional but make sure to include the `.` at the end.

- After the image is built run `docker run -p YOURDEVICEPORT:PORT_IN_CREDENTIALS_FILE NAME`. Where device port is whatever port you'll use on local host to play the game and NAME is whatever you named the image.

- You should get a notification the program is running in the terminal, after this navigate to the local host in your browser `127.0.0.1:PORTYOUPICKED/index` and you'll be greeted by the game. There are simple explanations along with this readme. 

- Once you are done you can quit the process in the terminal and delete the image. 

- If you have any questions feel free to email me at my email listed above.

## FAQ
### What is `src`?
This is a sub-package which contains modules related to the game. You should not make any changes there, but feel free to review them to get a better understanding.

### What is `data`?
This directory contains a few word lists in the form of text files. You should not make any changes to the ones that already exist. However, you can add your own (but don't have to). You can change the word list file in your `credentials.ini`.

### What is minijax?

`flask_minijax.py`, along with its template `templates/minijax.html`, is a tiny example of using JQuery with flask for an AJAX application. They should not be included in the version of the project you turn in. You can use this example to figure out how to implement an AJAX version of the game. Delete the two (along with `static/img`) when you're done with the project.

### How do I run the tests?
The `tests` directory contains a test suite for the `src` package. There's a `run_tests.sh`, which you can run in your container while it's running. However, it is not required, since you will not be changing anything in `src`.

## Grading Rubric

* If your code works as expected: 100 points. This includes:
	* AJAX in the frontend (`vocab.html`)
	* Logic in the backend (`flask_vocab.py`)
	* Frontend to backend interaction (with correct requests and responses) between `vocab.html` and `flask_vocab.py`.
	* Basically the webpage should handle validation WITHOUT any refreshes.
* If the game isn't fully functional as described, **40 point** will be docked.

* If messages are not displayed correctly in the webpage, 30 points will be docked. Expected behavior is notifying whether (a) the word typed is not in the vocabulary, or (b) the word cannot be made from the anagram; and in the case of a match, the word should be written somewhere along with the rest of the matched words.

* If none of the functionalities work, 30 will be assigned assuming
    * `credentials.ini` is submitted with the correct URL of your repo,
    * `Dockerfile` builds without any errors, and an instance runs without crashing.
    * `Dockerfile` and `README` are updated with your name and email.

* If the `Dockerfile` doesn't run, build or is missing, 5 will be assigned.

* If `credentials.ini` is not submitted or the repo is not found, 0 will be assigned.
	 

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.
