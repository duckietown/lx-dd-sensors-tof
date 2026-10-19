"""Duckiedrone ToF Sensors LX: student solution.

Subscribes to /DUCKIEDRONE_NAME/<sensor>_tof_driver_node/range
(``sensor_msgs/Range``) for each name in ``sensor_names`` and keeps the
newest reading from each sensor in ``latest_readings``. A throttled
logger prints them at ~1 Hz so students can verify the subscriber is
working.

Notebook 3 writes this node for the downward sensor. Notebook 4 points
it at all five.
"""

from collections.abc import Callable

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Range

from solution.tof_math import ToFReading, topics_for


class ToFSubscriber(Node):
    """Store and periodically log the most recent ToF readings."""

    def __init__(self) -> None:
        """Create the ToF subscriptions and timer-based logger."""
        super().__init__("tof_subscriber")

        # Step 1: read the node's parameters. The launch file sets them:
        # robot_namespace is the Duckiedrone's hostname. Notebook 4
        # extends sensor_names from ["bottom"] to all five sensors.
        self.declare_parameter("robot_namespace", "")
        self.declare_parameter("sensor_names", ["bottom"])
        self.declare_parameter("log_period_sec", 1.0)

        robot_parameter = self.get_parameter("robot_namespace")
        robot = robot_parameter.get_parameter_value().string_value
        sensor_names_parameter = self.get_parameter("sensor_names")
        sensor_names = list(
            sensor_names_parameter.get_parameter_value().string_array_value
        )
        log_period_parameter = self.get_parameter("log_period_sec")
        log_period = log_period_parameter.get_parameter_value().double_value

        # Every ToF topic starts with the hostname, as `ros2 topic list`
        # shows in Notebook 3.
        prefix = f"/{robot}" if robot else ""

        # Step 2: keep the newest reading from each sensor.
        # Key it by name, and keep the subscriptions themselves.
        self.latest_readings: dict[str, ToFReading] = {}
        self.subs = []

        # Step 3: create one subscription per sensor. topics_for turns
        # each name into the topic its bridge publishes on.
        for name, topic in zip(
            sensor_names, topics_for(sensor_names), strict=True
        ):
            full_topic = f"{prefix}{topic}"
            self.get_logger().info(
                f"Subscribing to {full_topic}  (sensor: {name})"
            )

            # ------------------------------------------------
            # TO IMPLEMENT: subscribe to this sensor's Range messages.
            # Activity 1 in Notebook 3 explains each argument.
            #
            # - Message type: Range.
            # - Topic: the `full_topic` variable above.
            # - Callback: self._make_callback(name), with parentheses.
            # - QoS profile: qos_profile_sensor_data.
            #
            # Append the returned subscription to self.subs.
            # ------------------------------------------------

        # Step 4: print on a timer, not from the callback. Notebook 3,
        # Activity 1 explains why the two are kept apart.
        self.create_timer(log_period, self.cb_log)

    def _make_callback(self, name: str) -> Callable[[Range], None]:
        """Create a callback that associates messages with ``name``."""

        # Step 5: build one callback per sensor. ROS 2 passes a callback
        # only the message, and header.frame_id is empty on a virtual
        # Duckiedrone. Capture the sensor name now and use it for every
        # message this callback receives.
        def cb_range(msg: Range) -> None:
            """Store the latest reading for this sensor."""
            # ------------------------------------------------
            # TO IMPLEMENT: unpack msg into self.latest_readings[name].
            # Activity 1 in Notebook 3 explains the fields.
            #
            # - Range: float(msg.range), in m.
            # - Timestamp: seconds plus nanoseconds times 1e-9.
            # - Frame: msg.header.frame_id.
            #
            # Store a ToFReading with sensor_name, stamp_sec,
            # range_m, and frame_id, replacing the `pass` below.
            # Do not print here.
            # ------------------------------------------------
            pass

        return cb_range

    def cb_log(self) -> None:
        """Log the most recently received ToF readings."""
        # Until the first message arrives there is nothing to print.
        # A node stuck here is the "When nothing arrives" case in
        # Notebook 3, Activity 2.
        if not self.latest_readings:
            self.get_logger().info("Waiting for ToF data...")
            return

        # Print one line with the newest range from each sensor.
        # Values below min_range and the 999.0 marker are not filtered
        # out (Notebook 3, Activity 3).
        parts = [
            f"{name}={reading.range_m:.3f}m"
            for name, reading in sorted(self.latest_readings.items())
        ]
        log_message = f"ranges=[{' '.join(parts)}]"
        self.get_logger().info(log_message)


def main(args: list[str] | None = None) -> None:
    """Run the ToF subscriber node until ROS 2 shuts down."""
    rclpy.init(args=args)
    node = ToFSubscriber()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
