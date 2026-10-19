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
sys.path.insert(0, str(REPO_ROOT / "packages" / "solution"))

from solution.tof_math import (  # noqa: E402
    OUT_OF_RANGE_FLAG,
    ToFReading,
    topics_for,
)

BOTTOM_RANGE_M = 0.50
EXPECTED_OUT_OF_RANGE_FLAG = 999.0


def _reading(sensor_name, range_m):
    return ToFReading(sensor_name=sensor_name, stamp_sec=0.0, range_m=range_m)


def test_reading_keeps_what_the_bridge_sent():
    reading = _reading("bottom", BOTTOM_RANGE_M)
    assert reading.sensor_name == "bottom"
    assert reading.range_m == BOTTOM_RANGE_M
    assert reading.frame_id == ""


def test_out_of_range_flag_matches_the_bridge():
    # The ROS 2 bridge publishes 999.0 in `range` when the driver has no distance.
    assert OUT_OF_RANGE_FLAG == EXPECTED_OUT_OF_RANGE_FLAG


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
