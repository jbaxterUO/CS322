"""
Nose tests for mongo.py

Write your tests HERE AND ONLY HERE.
"""
from mongo import insert_brevet, get_brevet
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_insert_one():
    controls = {"controls_list":
                [{"miles": "38.768", "km": "55", "location": "Paris", "start_time": "2023-01-01T00:00", "end_time":"2023-01-01T00:00"}]}

    insert_id = insert_brevet(controls)

    assert insert_id != "None"


def test_retrieve_one():

    controls = {"controls_list":
                [{"miles": "38.768", "km": "55", "location": "Paris", "start_time": "2023-01-01T00:00", "end_time":"2023-01-01T00:00"}]}

    id = insert_brevet(controls)
    controls_list = get_brevet()
    assert id != "None"
    assert controls_list["controls_list"][0]["miles"] == "38.768"
    assert controls_list["controls_list"][0]["km"] == "55"
    assert controls_list["controls_list"][0]["location"] == "Paris"
    assert controls_list["controls_list"][0]["start_time"] == "2023-01-01T00:00"
    assert controls_list["controls_list"][0]["end_time"] == "2023-01-01T00:00"