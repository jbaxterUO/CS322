"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
from acp_times import open_time, close_time
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_sub_sixty_km():
    brevet_dist = 200.0
    brevet_start_time = arrow.get("2023-01-01T00:00")
    check_points = {
        0: (brevet_start_time, brevet_start_time.shift(hours=1)),
        10:(brevet_start_time.shift(hours= 0, minutes= 18), brevet_start_time.shift(hours= 1, minutes= 30)),
        15:(brevet_start_time.shift(hours= 0, minutes= 26), brevet_start_time.shift(hours= 1, minutes= 45)),
        20:(brevet_start_time.shift(hours= 0, minutes= 35), brevet_start_time.shift(hours= 2, minutes= 0)),
        25:(brevet_start_time.shift(hours= 0 , minutes= 44), brevet_start_time.shift(hours= 2 , minutes= 15)),
        30:(brevet_start_time.shift(hours= 0, minutes= 53), brevet_start_time.shift(hours= 2, minutes= 30)),
        40:(brevet_start_time.shift(hours= 1, minutes= 11), brevet_start_time.shift(hours= 3, minutes= 0)),
        50:(brevet_start_time.shift(hours= 1, minutes= 28), brevet_start_time.shift(hours= 3, minutes= 30)),
        60:(brevet_start_time.shift(hours= 1, minutes= 46), brevet_start_time.shift(hours= 4, minutes= 0)),
    }

    for km, times in check_points.items():
        start_time, end_time = times
        assert open_time(km, brevet_dist, brevet_start_time) == start_time
        assert close_time(km, brevet_dist, brevet_start_time) == end_time


def test_mixed_200_km_():
    brevet_dist = 200.0
    brevet_start_time = arrow.get("2023-01-01T00:00")
    check_points = {
        60:(brevet_start_time.shift(hours= 1, minutes= 46), brevet_start_time.shift(hours= 4, minutes= 0)),
        100:(brevet_start_time.shift(hours= 2, minutes= 56), brevet_start_time.shift(hours= 6, minutes= 40)),
        120:(brevet_start_time.shift(hours= 3, minutes= 32), brevet_start_time.shift(hours= 8, minutes= 0)),
        160:(brevet_start_time.shift(hours= 4, minutes= 42), brevet_start_time.shift(hours= 10, minutes= 40)),
        200:(brevet_start_time.shift(hours= 5, minutes= 53), brevet_start_time.shift(hours= 13, minutes= 30)),
    }

    for km, times in check_points.items():
        start_time, end_time = times
        assert open_time(km, brevet_dist, brevet_start_time) == start_time
        assert close_time(km, brevet_dist, brevet_start_time) == end_time

def test_over_end_value_200_km():
    brevet_dist = 200.0
    brevet_start_time = arrow.get("2023-01-01T00:00")
    check_points = {
        240:(brevet_start_time.shift(hours= 5, minutes= 53), brevet_start_time.shift(hours= 13, minutes= 30)),
    }

    for km, times in check_points.items():
        start_time, end_time = times
        assert open_time(km, brevet_dist, brevet_start_time) == start_time
        assert close_time(km, brevet_dist, brevet_start_time) == end_time


def test_over_end_value_600_km():
    brevet_dist = 600.0
    brevet_start_time = arrow.get("2023-01-01T00:00")
    check_points = {
        720:(brevet_start_time.shift(hours= 18, minutes= 48), brevet_start_time.shift(hours= 40, minutes= 0)),
    }

    for km, times in check_points.items():
        start_time, end_time = times
        assert open_time(km, brevet_dist, brevet_start_time) == start_time
        assert close_time(km, brevet_dist, brevet_start_time) == end_time
    

def test_higher_km_mixed():
    brevet_dist = 1000.0
    brevet_start_time = arrow.get("2023-01-01T00:00")
    check_points = {
        720:(brevet_start_time.shift(hours= 23, minutes= 5), brevet_start_time.shift(hours= 50, minutes= 30)),
        890:(brevet_start_time.shift(hours= 29, minutes= 9), brevet_start_time.shift(hours= 65, minutes= 23)),
        950:(brevet_start_time.shift(hours= 31, minutes= 18), brevet_start_time.shift(hours= 70, minutes= 38)),
        1000:(brevet_start_time.shift(hours= 33, minutes= 5), brevet_start_time.shift(hours= 75, minutes= 0)),
    }

    for km, times in check_points.items():
        start_time, end_time = times
        assert open_time(km, brevet_dist, brevet_start_time) == start_time
        assert close_time(km, brevet_dist, brevet_start_time) == end_time