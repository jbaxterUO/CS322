"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
from mongo import insert_brevet, get_brevet
import config

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
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
    /_submit: inserts a list of control points in a brevet into the database.

    Gets json and responds with json via POST requests only.
    """

    try:

        input_json = request.json

        brevet = input_json["controls_list"]

        brevet_id = insert_brevet(brevet)

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

    try:
        controls_list = get_brevet()
        return flask.jsonify(
            controls_list=controls_list,
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

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
