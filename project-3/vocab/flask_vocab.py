"""
Flask web site with vocabulary matching game
(identify vocabulary words that can be made
from a scrambled string)
"""

import flask
import logging

# Our modules
from src.letterbag import LetterBag
from src.vocab import Vocab
from src.jumble import jumbled
import src.config as config

from flask import request


###
# Globals
###
session_set = False
app = flask.Flask(__name__)

CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY  # Should allow using session variables


#
# One shared 'Vocab' object, read-only after initialization,
# shared by all threads and instances.  Otherwise we would have to
# store it in the browser and transmit it on each request/response cycle,
# or else read it from the file on each request/responce cycle,
# neither of which would be suitable for responding keystroke by keystroke.

WORDS = Vocab(CONFIG.VOCAB)
SEED = CONFIG.SEED
try:
    SEED = int(SEED)
except ValueError:
    SEED = None


###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
    """The main page of the application"""
    flask.g.vocab = WORDS.as_list()
    flask.session["session_set"] = 'Yes'
    flask.session["target_count"] = min(
    len(flask.g.vocab), CONFIG.SUCCESS_AT_COUNT)
    flask.session["jumble"] = jumbled(
    flask.g.vocab, flask.session["target_count"], seed=None if not SEED or SEED < 0 else SEED)
    flask.session["matches"] = []
    app.logger.debug("Session variables have been set")
    assert flask.session["matches"] == []
    assert flask.session["target_count"] > 0
    app.logger.debug("At least one seems to be set correctly")
    return flask.render_template('vocab.html')


@app.route("/success")
def success():
    return flask.render_template('success.html')


#######################
# Form handler.
#   You'll need to change this to a
#   a JSON request handler
#######################

@app.route("/_check")
def check():
    """
    User has typed a valid letter. We check if the current string
    is a possible word and if it is we check if it can be made with the current
    jumble. If both are achieved the word is added to the match list. After num_matches
    set in the credentials.ini/default.ini the game ends.
    """
    app.logger.debug("Entering check")

    # The data we need, from form and from cookie
    text = request.args.get('text', str)
    jumble = flask.session["jumble"]
    matches =flask.session.get("matches", [])  # Default to empty list

    # Is it good?
    in_jumble = LetterBag(jumble).contains(text)
    matched = WORDS.has(text)

    #By default a ping won't have a new word, only one case changes that
    #So this variable is set to false up here as default and only changed
    #In the one case where a new word is found

    newWord = {"newWord":False};

    # Respond appropriately
    if matched and in_jumble and not (text in matches):
        # Cool, they found a new word
        matches.append(text)

        flask.session["matches"] = matches

        message = {"message": "{} is in the list of words, nice job!".format(text)}
        #Used only to keep track of if the form should be cleared or not
        isWord = {"word": True}
        newWord = {"newWord": True}
    elif text in matches:
        message = {"message": "You already found {}".format(text)}
        isWord = {"word": True}
    elif not matched:
        message = {"message": "{} isn't in the list of words".format(text)}
        isWord = {"word": False}
    elif not in_jumble:
        message = {"message":'"{}" can\'t be made from the letters {}'.format(text, jumble)}
        isWord = {"word": True}
    else:
        app.logger.debug("This case shouldn't happen!")
        assert False  # Raises AssertionError

    #Create list of matched words to send back to be printed
    wordList = {"wordList": flask.session['matches']}

    # Check outcome:  Solved enough, or keep going?
    if len(matches) >= flask.session["target_count"]:
        gameOver = {"gameOver": True}
        return flask.jsonify(gameOver=gameOver)
    else:
        gameOver = {"gameOver": False}
        return flask.jsonify(
                            isWord=isWord, wordList=wordList, message=message, 
                            gameOver=gameOver, newWord=newWord)





###################
#   Error handlers
###################


@app.errorhandler(404)
def error_404(e):
    app.logger.warning("++ 404 error: {}".format(e))
    return flask.render_template('404.html'), 404


@app.errorhandler(500)
def error_500(e):
    app.logger.warning("++ 500 error: {}".format(e))
    assert not True  # I want to invoke the debugger
    return flask.render_template('500.html'), 500


@app.errorhandler(403)
def error_403(e):
    app.logger.warning("++ 403 error: {}".format(e))
    return flask.render_template('403.html'), 403


#############

if __name__ == "__main__":
    if CONFIG.DEBUG:
        app.debug = True
        app.logger.setLevel(logging.DEBUG)
        app.logger.info(
            "Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0", debug=CONFIG.DEBUG)
