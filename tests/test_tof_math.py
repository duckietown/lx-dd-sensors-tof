"""Sanity tests for the Duckiedrone ToF student solution.

Run from the LX root with:

    pytest tests/

These tests import ``solution.tof_math``, a pure-Python module with no
ROS dependency, so they can run both inside the editor container and
on a plain host Python.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / 'packages' / 'solution'))

from solution.tof_math import (  # noqa: E402
    OUT_OF_RANGE_FLAG,
    ToFReading,
    topics_for,
)


def _reading(name, r):
    return ToFReading(sensor_name=name, stamp_sec=0.0, range_m=r)


def test_reading_keeps_what_the_bridge_sent():
    r = _reading("bottom", 0.50)
    assert r.sensor_name == "bottom"
    assert r.range_m == 0.50
    assert r.frame_id == ""


def test_out_of_range_flag_matches_the_bridge():
    # The ROS 2 bridge publishes 999.0 in `range` when the driver has no distance.
    assert OUT_OF_RANGE_FLAG == 999.0


def test_topics_for_single_sensor():
    assert topics_for(["bottom"]) == ["/bottom_tof_driver_node/range"]


def test_topics_for_all_five_sensors():
    assert topics_for(["bottom", "front", "left", "right", "top"]) == [
        "/bottom_tof_driver_node/range",
        "/front_tof_driver_node/range",
        "/left_tof_driver_node/range",
        "/right_tof_driver_node/range",
        "/top_tof_driver_node/range",
    ]


def test_topics_for_no_sensors():
    assert topics_for([]) == []
