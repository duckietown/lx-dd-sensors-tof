"""Pure-Python ToF helpers.

This module has no ROS 2 dependency on purpose, so it can be imported
from a plain Python interpreter (e.g. from the tests) without needing
``rclpy``. The ROS 2 subscriber in ``tof_subscriber.py`` re-uses these
helpers.
"""

from dataclasses import dataclass


# What the ROS 2 bridge puts in ``range`` when the driver has no distance to
# report (Notebook 2, Step 3). It is far above max_range, which marks the reading
# as one to discard.
OUT_OF_RANGE_FLAG = 999.0


# One reading, as the callback in tof_subscriber.py stores it: which sensor it
# came from, when the driver read it, the range, and the frame it was measured in.
@dataclass
class ToFReading:
    sensor_name: str
    stamp_sec: float   # seconds since the epoch, from header.stamp
    range_m: float     # in m, or OUT_OF_RANGE_FLAG
    frame_id: str = ""


def topics_for(sensor_names: list) -> list:
    """Return the topic each ToF bridge publishes on, one per sensor name."""
    # ------------------------------------------------------------------
    # TO IMPLEMENT: build one topic per name. Notebook 4, Activity 2
    # explains the pattern.
    #
    #   ['bottom', 'front'] -> ['/bottom_tof_driver_node/range',
    #                           '/front_tof_driver_node/range']
    #
    # Leave out the /<robot> prefix; ToFSubscriber adds it.
    # ------------------------------------------------------------------
    # Until this is written, only the bottom sensor's topic comes back, which
    # is all Notebook 3 needs.
    return ['/bottom_tof_driver_node/range']
