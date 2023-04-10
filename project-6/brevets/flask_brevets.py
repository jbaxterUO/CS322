"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
import os
from flask import request
import requests
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import logging

###
# Globals
###
app = flask.Flask(__name__)

######################################
########### API Calls ################
######################################

API_ADDR = os.environ["API_ADDR"]
API_PORT = os.environ["API_PORT"]
API_URL = f"http://{API_ADDR}:{API_PORT}/api/"


def get_brevet():
    #Call to API to get all brevets in the database, temp is the most recent brevet entered
    temp = requests.get(f"{API_URL}/brevets").json()[-1]
    
    #Take db entry and convert important info into a dictionary to be returned
    #This is done because temp also has a field "id" that we don't want returned with the info
    brevet = {"length":temp["length"], "start_time":temp["start_time"], "checkpoints":temp["checkpoints"]}
    return brevet

def insert_brevet(brevet):
    response = requests.post(f"{API_URL}/brevets", json=brevet)
    #Response.txt is the text given in the Response object generated from our API call
    #In this case it end up being a dictionary of the form {"_id": "UNIQUE_ID"}
    _id = response.text
    return _id
###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('calc.html')

@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404

###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    error_message = "None"
    km = request.args.get('km', 0, type=float)
    time = request.args.get('start_date', "",type=str)

    if time == "":
        start_time = arrow.now().isoformat()
        time = arrow.now().isoformat().format("YYYY-MM-DDTHH:mm")
    else:
        start_time = arrow.get(time)

    brevet_dist = request.args.get('brevet_dist', type=int)
    if km < 0:
        error_message =f"The control point must be a positive distance away instead of {km}km."
    elif km > (.20 * brevet_dist) + brevet_dist:
        error_message = f"The control can't be larger than 20 percent of the Brevet. For a Brevet of {brevet_dist}km that would be {(.20 * brevet_dist) + brevet_dist}km."
    
    open_time = acp_times.open_time(km, brevet_dist, start_time).format("YYYY-MM-DDTHH:mm")
    close_time = acp_times.close_time(km, brevet_dist, start_time).format("YYYY-MM-DDTHH:mm")
    result = {"open": open_time, "close": close_time}
    e_message = {"e_message": error_message}
    date = {"date": time}
    
    return flask.jsonify(result=result, error=e_message, date=date)

@app.route("/_submit", methods=["POST"])
def submit():
    """
    /_submit: inserts a list of control points in a brevet into the database via a RESTful API.

    Uses insert_brevet to interact with API where insert_brevet expects a dictionary of the form

    input_json = {
        length: int
        start_time: datetime
        checkpoints: list of dicts[{open_time: datetime, close_time: datetime, distance: float, location: string}]
        }

    Response from API is a unique identifier in a dict in the form {_id = unique id}
    """

    try:
        #Modify input from request into python dictionary, then pass to api for storage
        input_json = request.json
        brevet_id = insert_brevet(input_json)

        return flask.jsonify(result={},
                             message="Inserted!",
                             status=1,
                             mongo_id=brevet_id)
    except:
        return flask.jsonify(result={},
                             message="Server, error!",
                             status=0,
                             mongo_id ='None')

@app.route("/_display")
def display():
    """
    /_display: retrieves the last inserted brevet from the database via a RESTful API.

    Uses get_brevet to interact with API where get_brevet expects no arguments.

    Response from API is a dictionary of the form:

    brevet = {
        length: int
        start_time: datetime
        checkpoints: list of dicts[{open_time: datetime, close_time: datetime, distance: float, location: string}]
        }

    """

    try:
        #Get brevet from database
        brevet = get_brevet()
        return flask.jsonify(
            brevet=brevet,
            status=1,
            messge="Successfully fetched brevet."
        )
    
    except:
        return flask.jsonify(
            result={},
            status=0,
            message="Error, something went wrong."
        )
    
#############
app.debug = True if "DEBUG" not in os.environ else os.environ["DEBUG"]
port_num = os.environ["PORT"]

if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(port_num))
    app.run(port=port_num, host="0.0.0.0")
