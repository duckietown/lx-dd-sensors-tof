"""Pure-Python ToF helpers.

This module has no ROS 2 dependency on purpose, so it can be imported
from a plain Python interpreter (e.g., from the tests) without needing
``rclpy``. The ROS 2 subscriber in ``tof_subscriber.py`` re-uses these
helpers.
"""

from dataclasses import dataclass

# What the ROS 2 bridge puts in ``range`` when the driver has no
# distance to report (Notebook 2, Step 3). It is far above max_range,
# which marks the reading as one to discard.
OUT_OF_RANGE_FLAG = 999.0


@dataclass
class ToFReading:
    """Decoded ToF sample in ROS-compatible units."""

    sensor_name: str
    stamp_sec: float  # Seconds since the epoch, from header.stamp.
    range_m: float  # In m, or OUT_OF_RANGE_FLAG.
    frame_id: str = ""


def topics_for(sensor_names: list[str]) -> list[str]:
    """Return one ToF bridge topic for each sensor name."""
    # ------------------------------------------------------------------
    # TO IMPLEMENT: build one topic per name. Notebook 4, Activity 2
    # explains the pattern.
    #
    #   ["bottom", "front"] -> ["/bottom_tof_driver_node/range",
    #                              "/front_tof_driver_node/range"]
    #
    # Leave out the /DUCKIEDRONE_NAME prefix; ToFSubscriber adds it.
    # ------------------------------------------------------------------
    # Until this is written, only the bottom sensor's topic comes back,
    # which is all Notebook 3 needs.
    return ["/bottom_tof_driver_node/range"]
