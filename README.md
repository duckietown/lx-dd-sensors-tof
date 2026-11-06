<p align="center">
<a href="https://duckietown.com"><img src="./assets/images/dtlogo.png" alt="Duckietown Logo" width="30%"></a>
</p>

# Learning Experience (LX): Duckiedrone ToF Sensors

`Software: ente`; `Hardware: DD24-B`

The Duckiedrone's five time-of-flight (ToF) sensors measure distances to surfaces below,
above, ahead, and on either side of the Duckiedrone. The downward reading contributes to height
estimation, while the other four provide observations of nearby surfaces. Their usefulness depends
on the target, lighting, acquisition settings, and how recently each reading arrived. This learning
experience (LX) investigates those conditions, measures accuracy against an independent reference,
and follows the readings into a ROS 2 program that receives data from one or all five sensors.

## Intended learning outcomes

After completing this LX, learners will be able to:

1. Explain how a ToF sensor estimates distance and how target properties, ambient light, and acquisition settings affect its readings.

2. Record stationary measurements and compare their mean and median with an independently measured reference, reporting signed mean error, sample standard deviation, and rejected-reading fraction.

3. Trace a reading from the sensor to a ROS 2 topic, identifying where its units, timestamp, and range bounds are determined and distinguishing configured frequency from observed arrival rate.

4. Interpret a `sensor_msgs/msg/Range` message using its range bounds, scene geometry, and timing.

5. Complete, deploy, and run the supplied ROS 2 subscriber for one or all five sensors, explaining how callbacks update readings and a timer displays the stored values.

## Run this LX

Follow the Duckietown Manual's [LX General Instructions](https://docs.duckietown.com/ente/opmanual-dd24/50-learning-experiences/lx-general-procedure.html)
to open the LX in its prepared editor environment. Work through the notebooks in order.

## Notebooks

| # | Notebook | Investigation |
| --- | --- | --- |
| 1 | [Time-of-Flight (ToF) Sensor Fundamentals](./notebooks/1-tof-basics.ipynb) | Inspect a reported range, explore a photon-count model, and interpret a stationary recording. |
| 2 | [Measuring ToF sensor accuracy](./notebooks/2-measuring-tof-sensor-accuracy.ipynb) | Compare recorded ranges with a ruler measurement and characterize agreement, repeatability, and usable-reading availability. |
| 3 | [Duckiedrone ToF Sensor Architecture](./notebooks/3-duckiedrone-tof-architecture.ipynb) | Trace readings through the driver, bridge, and flight-controller path; inspect configuration and message rates. |
| 4 | [Subscribing to the ToF sensor data](./notebooks/4-subscribing-to-tof.ipynb) | Complete the downward-range subscriber and relate its periodic display to arriving measurements. |
| 5 | [All Five Sensors](./notebooks/5-all-five-sensors.ipynb) | Start the additional sensor services, extend the subscriber, and interpret independently updated readings together. |

## Prerequisites

Complete the Duckietown Manual's [Initial Setup](https://docs.duckietown.com/ente/opmanual-dd24/10-duckiedrone-preliminaries/initial-setup.html#required-software-and-accounts)
so Docker and the Duckietown Shell (`dts`) are installed and configured on the base station.
Use the supported native Ubuntu setup or a Duckietown Workspace on macOS or Windows.
The activities assume familiarity with Python functions, lists, and dictionaries, and with the
basic ROS 2 topic and subscriber concepts introduced in the preceding LXs.

The model and supplied recording in
[Time-of-Flight (ToF) Sensor Fundamentals](./notebooks/1-tof-basics.ipynb)
can be explored without a connected Duckiedrone. Live topic inspection, driver configuration,
and subscriber activities require a physical or virtual Duckiedrone running the `ente` stack.

[Measuring ToF sensor accuracy](./notebooks/2-measuring-tof-sensor-accuracy.ipynb)
requires a physical Duckiedrone, a ruler, a broad flat target, and stable supports that leave the
sensor's field of view clear. The Duckiedrone box can serve as a support or target. A virtual
Duckiedrone supports practice with collection and analysis using simulated geometry; physical
sensor characterization and acquisition-setting comparisons use the physical hardware.

### Choose the terminal

The base station is the computer or Workspace environment running the device-facing `dts`
commands. Keep a separate base-station terminal available alongside the LX editor. The editor
has its own filesystem and execution environment; recordings downloaded to the base station
must also be made available in the editor's `assets/data/` directory.

| Task | Where to run it |
| --- | --- |
| Read notebooks, run their Python cells, and edit the supplied source files | The LX editor opened through the general instructions |
| Connect to the Duckiedrone, run `dts stack`, `dts code build`, or `dts code workbench`, and download a recording with `scp` | A separate base-station terminal in the LX project folder |
| Inspect Docker containers, copy recordings out with `docker cp`, or edit physical driver configuration | The Duckiedrone device shell |
| Inspect or record ToF messages with `ros2 topic` | A shell inside the Duckiedrone's `ros2-tof-bottom` bridge container |
| Watch the listener output and stop a workbench run with `Ctrl+C` | The terminal running `dts code workbench` |

The connection and bridge-shell steps are introduced in
[Time-of-Flight (ToF) Sensor Fundamentals](./notebooks/1-tof-basics.ipynb#gathering-tof-measurements-from-a-duckiedrone).
Replace `DUCKIEDRONE_NAME` in commands with the configured Duckiedrone name, and use the topic
namespace shown by `ros2 topic list`.

### Physical and virtual operation

Keep a physical Duckiedrone disarmed with its motors stopped during these activities.
For a virtual Duckiedrone, start the Duckiematrix and attach the Duckiedrone to an entity before
expecting simulated ToF messages. Follow the
[Duckiematrix setup instructions](https://docs.duckietown.com/ente/duckietown-manual/50-duckiematrix/getting-started/duckiematrix-first-steps.html).

The standard stack starts the bottom sensor.
[All Five Sensors](./notebooks/5-all-five-sensors.ipynb#activity-1)
explains how to start the four additional driver/bridge pairs and check their streams.
Record the original service state and settings before experiments, then restore them afterward.

### Notebooks and checkpoints

Run the notebooks in the prepared LX editor. The self-check cells use the active notebook's
identity supplied by that editor to load their questions. Enter a response before revealing
the model answer.

## Code activities

[Subscribing to the ToF sensor data](./notebooks/4-subscribing-to-tof.ipynb)
guides the two `TO IMPLEMENT` blocks in
[tof_subscriber.py](./packages/solution/solution/tof_subscriber.py).
[All Five Sensors](./notebooks/5-all-five-sensors.ipynb)
extends the topic list in [tof_math.py](./packages/solution/solution/tof_math.py)
and changes the sensor selection in
[the launch file](./packages/tof_listener/launch/tof_listener_node.launch.py).
The solution checkout already contains the subscriber and topic-helper implementations;
its launch default selects the bottom sensor. Follow the notebooks to select all five, save
changes, build, and run the workbench.

## Further reading

Each notebook links to the sources relevant to its lesson. The main references are:

- [VL53L1X datasheet](https://www.st.com/resource/en/datasheet/vl53l1x.pdf): sensor characteristics and ranging performance under specified conditions.

- [ROS 2 Range message definition](https://github.com/ros2/common_interfaces/blob/jazzy/sensor_msgs/msg/Range.msg): fields, units, and range validity rules.

## For LX authors

Learner material is in `notebooks/` and `packages/`; checkpoint prompts and model answers are in
`checkpoint_data/`, and structural and subscriber checks are in `tests/`. Run checks from the LX root:

```bash
python3 -m pytest tests/
ruff check .
```
