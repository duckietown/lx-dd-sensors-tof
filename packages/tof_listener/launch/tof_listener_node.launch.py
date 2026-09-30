#!/usr/bin/env python3
"""Launch file for the Duckiedrone ToF listener node.

Usage
-----
ros2 launch tof_listener tof_listener_node.launch.py robot_namespace:=<ROBOT>

Parameters
----------
robot_namespace : str       Duckiedrone hostname (the ToF topic namespace).
                            Defaults to the VEHICLE_NAME environment variable.
sensor_names    : str list  ToF sensors to subscribe to. Defaults to ['bottom'],
                            the one sensor a Duckiedrone runs by default.
log_period_sec  : float     How often the listener prints a summary line.
                            Defaults to 1.0 s.
"""

import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    robot_namespace_arg = DeclareLaunchArgument(
        'robot_namespace',
        default_value=os.environ.get('VEHICLE_NAME', ''),
        description='Namespace used by the ToF bridges (the Duckiedrone hostname).',
    )

    # Notebook 4, Activity 2 changes this default to all five sensors:
    # "['bottom','front','left','right','top']"
    sensor_names_arg = DeclareLaunchArgument(
        'sensor_names',
        default_value="['bottom']",
        description='Names of the ToF sensors to subscribe to.',
    )

    log_period_arg = DeclareLaunchArgument(
        'log_period_sec',
        default_value='1.0',
        description='Seconds between summary log lines.',
    )

    tof_listener_node = Node(
        package='tof_listener',
        executable='tof_listener_node',
        name='tof_listener_node',
        output='screen',
        emulate_tty=True,
        parameters=[{
            'robot_namespace': LaunchConfiguration('robot_namespace'),
            'sensor_names': LaunchConfiguration('sensor_names'),
            'log_period_sec': LaunchConfiguration('log_period_sec'),
        }],
    )

    return LaunchDescription([
        robot_namespace_arg,
        sensor_names_arg,
        log_period_arg,
        tof_listener_node,
    ])
