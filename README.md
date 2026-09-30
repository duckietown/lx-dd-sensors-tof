# Duckiedrone ToF Sensors - Learning Experience

`Software: ente`; `Hardware: DD24-B`

A time-of-flight sensor measures the distance to a surface from the light that surface reflects back. The Duckiedrone carries five: one pointing down, one pointing up, and three pointing horizontally to the front, left, and right. Its flight controller takes its height from the distance the downward one measures. This Learning Experience covers how the sensor turns detected light into a distance and when it cannot, how a reading reaches a ROS 2 topic, and how to write the node that reads it.

## Intended learning outcomes

After completing this learning experience, learners will be able to:

1. Explain how a time-of-flight sensor recovers a distance, and predict how its maximum range changes with the surface it is pointed at, the ambient light, and its timing budget.

2. Trace a range reading from the sensor chip to a ROS 2 topic, naming what each step changes and what sets its rate.

3. Read a `sensor_msgs/Range` message from a Duckiedrone and tell a usable distance apart from a reading to discard.

4. Write, deploy, and run a ROS 2 node on a Duckiedrone that subscribes to one ToF topic, then to all five.

## Notebooks

Go through these in order:

| # | Notebook | Description |
| --- | --- | --- |
| 1 | `1-tof-basics.ipynb` | What a time-of-flight sensor measures, how the VL53L1X measures it, and when it cannot |
| 2 | `2-duckiedrone-tof-architecture.ipynb` | The path from the VL53L1X to `/<robot>/<sensor>_tof_driver_node/range`, and where its settings live |
| 3 | `3-subscribing-to-tof.ipynb` | Write, deploy, and run a ROS 2 node that reads a ToF topic |
| 4 | `4-all-five-sensors.ipynb` | Start the other four sensors and read all five with the same node |

## What you need

A Duckiedrone, physical or virtual, running the `ente` software stack.

On a virtual Duckiedrone, the Duckiematrix has to be running, with the Duckiedrone attached to an entity, before the ToF topics carry data.
