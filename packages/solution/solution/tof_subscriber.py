"""Duckiedrone ToF Sensors LX: student solution.

Subscribes to /<robot>/<sensor>_tof_driver_node/range (sensor_msgs/Range) for
each name in ``sensor_names`` and keeps the newest reading from each sensor in
``latest_readings``. A throttled logger prints them at ~1 Hz so students can
verify the subscriber is working.

Notebook 3 writes this node for the downward sensor; Notebook 4 points it at
all five.
"""

from typing import Dict

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Range

from solution.tof_math import ToFReading, topics_for


class ToFSubscriber(Node):

    def __init__(self):
        super().__init__('tof_subscriber')

        # Step 1: read the node's parameters. The launch file sets them:
        # robot_namespace is the Duckiedrone's hostname, and sensor_names is the
        # list Notebook 4 extends from ['bottom'] to all five sensors.
        self.declare_parameter('robot_namespace', '')
        self.declare_parameter('sensor_names', ['bottom'])
        self.declare_parameter('log_period_sec', 1.0)

        robot = self.get_parameter('robot_namespace').get_parameter_value().string_value
        names = list(self.get_parameter('sensor_names').get_parameter_value().string_array_value)
        log_period = self.get_parameter('log_period_sec').get_parameter_value().double_value

        # Every ToF topic starts with the hostname, as `ros2 topic list` shows in
        # Notebook 3.
        prefix = f'/{robot}' if robot else ''

        # Step 2: somewhere to keep the newest reading from each sensor, keyed by
        # sensor name, and the subscriptions themselves.
        self.latest_readings: Dict[str, ToFReading] = {}
        self.subs = []

        # Step 3: one subscription per sensor. topics_for turns each sensor name
        # into the topic its bridge publishes on.
        for name, topic in zip(names, topics_for(names)):
            full_topic = f'{prefix}{topic}'
            self.get_logger().info(f'Subscribing to {full_topic}  (sensor: {name})')

            # ------------------------------------------------------------------
            # TO IMPLEMENT: ask ROS 2 for this sensor's messages. Notebook 3,
            # Activity 1 explains why each argument is what it is.
            #
            #   sub = self.create_subscription(<type>, <topic>, <cb>, <qos>)
            #
            #     <type>   Range
            #     <topic>  the `full_topic` variable above
            #     <cb>     self._make_callback(name), with parentheses
            #     <qos>    qos_profile_sensor_data
            #
            # Append `sub` to self.subs.
            # ------------------------------------------------------------------

        # Step 4: print on a timer, not from the callback. Notebook 3, Activity 1
        # explains why the two are kept apart.
        self.create_timer(log_period, self.cb_log)

    def _make_callback(self, name: str):
        # Step 5: build one callback per sensor. ROS 2 passes a callback only the
        # message, and header.frame_id is empty on a virtual Duckiedrone, so the
        # sensor's name is captured here, when the callback is created, and used
        # later each time a message arrives.
        def cb_range(msg: Range) -> None:
            # --------------------------------------------------------------
            # TO IMPLEMENT: unpack `msg` into self.latest_readings[name],
            # which cb_log reads when it prints. Notebook 3, Activity 1
            # explains the fields.
            #
            #   range_m    float(msg.range)                       m
            #   stamp_sec  msg.header.stamp.sec + msg.header.stamp.nanosec * 1e-9
            #   frame_id   msg.header.frame_id
            #
            # Store them as ToFReading(sensor_name=name, stamp_sec=...,
            # range_m=..., frame_id=...), replacing the `pass` below. Do not
            # print here.
            # --------------------------------------------------------------
            pass

        return cb_range

    def cb_log(self) -> None:
        # Until the first message arrives there is nothing to print. A node stuck
        # here is the "When nothing arrives" case in Notebook 3, Activity 2.
        if not self.latest_readings:
            self.get_logger().info('Waiting for ToF data...')
            return

        # One line with the newest range from each sensor, printed as it arrived:
        # values below min_range and the 999.0 marker are not filtered out
        # (Notebook 3, Activity 3).
        parts = [f'{name}={r.range_m:.3f}m' for name, r in sorted(self.latest_readings.items())]
        self.get_logger().info(f'ranges=[{" ".join(parts)}]')


def main(args=None):
    # Start ROS 2, create the node, and hand it to rclpy.spin, which calls the
    # callbacks and the timer until Ctrl-C stops it.
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


if __name__ == '__main__':
    main()
