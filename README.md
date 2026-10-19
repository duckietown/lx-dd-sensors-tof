<p align="center">
<a href="https://duckietown.com"><img src="./assets/images/dtlogo.png" alt="Duckietown Logo" width="50%"></a>
</p>

# Learning Experience (LX): Duckiedrone ToF Sensors

`Software: ente`; `Hardware: DD24-B`

A time-of-flight (ToF) sensor estimates distance from light returned by a surface. The Duckiedrone
carries five: one pointing down, one up, and three horizontally to the front, left, and right. The
downward reading provides the flight controller with a height cue, not an absolute altitude. This
learning experience (LX) covers how the sensor measures distance and its limits, how a reading
reaches a ROS 2 topic, and how to subscribe to one or all five sensors.

## Intended learning outcomes

After completing this LX, learners will be able to:

1. Explain how a time-of-flight sensor recovers a distance, and predict how its maximum range changes with the surface it is pointed at, the ambient light, and its timing budget.

2. Trace a range reading from the sensor chip to a ROS 2 topic, naming what each step changes and what sets its rate.

3. Read a `sensor_msgs/Range` message from a Duckiedrone and tell a usable distance apart from a reading to discard.

4. Write, deploy, and run a ROS 2 node on a Duckiedrone that subscribes to one ToF topic, then to all five.

## Run this LX

Follow the Duckietown Manual's [LX General Instructions](https://docs.duckietown.com/ente/opmanual-dd24/50-learning-experiences/lx-general-procedure.html) to open this LX in a prepared environment. The notebooks provide the topic-specific activities; the prerequisites below describe the local setup.

## Notebooks

Start with [Notebook 1](./notebooks/1-tof-basics.ipynb) for the sensor model and measurement
limits. [Notebook 2](./notebooks/2-duckiedrone-tof-architecture.ipynb) traces the data to a ROS 2
topic. [Notebook 3](./notebooks/3-subscribing-to-tof.ipynb) builds a downward-range listener;
[Notebook 4](./notebooks/4-all-five-sensors.ipynb) starts the remaining services and extends it to
all five sensors.

| # | Notebook | Description |
| --- | --- | --- |
| 1 | [Notebook 1](./notebooks/1-tof-basics.ipynb) | What a time-of-flight sensor measures, how the VL53L1X measures it, and when it cannot |
| 2 | [Notebook 2](./notebooks/2-duckiedrone-tof-architecture.ipynb) | The path from the VL53L1X to `/DUCKIEDRONE_NAME/<sensor>_tof_driver_node/range`, and where its settings live |
| 3 | [Notebook 3](./notebooks/3-subscribing-to-tof.ipynb) | Write, deploy, and run a ROS 2 node that reads a ToF topic |
| 4 | [Notebook 4](./notebooks/4-all-five-sensors.ipynb) | Start the other four sensors and read all five with the same node |

## Prerequisites

Complete the Duckietown Manual's [Initial Setup](https://docs.duckietown.com/ente/opmanual-dd24/10-duckiedrone-preliminaries/initial-setup.html#required-software-and-accounts)
so Docker and the Duckietown Shell (`dts`) are installed and configured on the base station.
Notebooks 1 and 2 use a model and architectural explanations without a live Duckiedrone;
[Notebooks 3](./notebooks/3-subscribing-to-tof.ipynb) and
[4](./notebooks/4-all-five-sensors.ipynb) require a virtual or physical Duckiedrone running the
`ente` software stack.

The base station is the computer running Docker and `dts`. The `dts code editor` terminal belongs
to a separate browser-editor environment: its filesystem and `localhost` are not the base station's.
Keep a separate base-station terminal available for device commands.

### Choose the terminal

| Task | Where to run it |
| --- | --- |
| Read notebooks, run the model in [Notebook 1](./notebooks/1-tof-basics.ipynb), and edit [tof_subscriber.py](./packages/solution/solution/tof_subscriber.py), [tof_math.py](./packages/solution/solution/tof_math.py), and [the launch file](./packages/tof_listener/launch/tof_listener_node.launch.py) | `dts code editor` |
| Run `dts duckiebot virtual connect`, `dts stack up` or `down`, `dts code build`, `dts code workbench`, or physical-device `ssh` | A separate base-station terminal, outside `dts code editor` |
| Inspect `/DUCKIEDRONE_NAME/bottom_tof_driver_node/range` with `ros2 topic` in [Notebook 3](./notebooks/3-subscribing-to-tof.ipynb) | The authorized Duckiedrone's ToF bridge container shell, reached after connecting to the device |
| Watch listener output and stop a live run | The original workbench terminal; keep it ready for `Ctrl-C` |

### Local notebooks and checkpoints

Open the notebooks in `dts code editor`. Interactive checkpoints require notebook metadata supplied
by that editor; a Jupyter/IPython kernel with `ipywidgets` alone is not sufficient. The sensor model
in Notebook 1 can be explored before a Duckiedrone is available.

### Virtual or physical Duckiedrone

For a virtual Duckiedrone, start the Duckiematrix and attach the Duckiedrone to an entity you are
authorized to operate before expecting ToF topics to carry data. For a physical DD24-B Duckiedrone,
use the `ente` services described in [Notebook 3](./notebooks/3-subscribing-to-tof.ipynb). This LX
does not arm or fly the Duckiedrone; handle a physical device only while disarmed and clear of the
propellers.

### Authorized device access

Use only hardware, credentials, and a network path that its owner or administrator has explicitly
authorized. Notebooks 3 and 4 connect to the Duckiedrone, and starting four extra sensor services
in Notebook 4 changes its running configuration.

## Complete the ToF subscriber

Fill the two `TO IMPLEMENT` blocks in [tof_subscriber.py](./packages/solution/solution/tof_subscriber.py)
to subscribe to and unpack downward `Range` messages as described in
[Notebook 3](./notebooks/3-subscribing-to-tof.ipynb). [Notebook 4](./notebooks/4-all-five-sensors.ipynb)
starts the other four sensor services, adds topic names in
[tof_math.py](./packages/solution/solution/tof_math.py), and updates
[the launch file](./packages/tof_listener/launch/tof_listener_node.launch.py) to listen to all five.
From the LX root in the base-station terminal, build and run the listener on an authorized device:

```bash
dts code build -R DUCKIEDRONE_NAME
dts code workbench -R DUCKIEDRONE_NAME
```

The workbench displays the listener's output. Keep the additional sensor services running during
Notebook 4's activities, and stop them afterward as that notebook directs.

## Further reading

Each notebook's Further reading section is the primary reference for its lesson. These sources
cover the main stages of this LX:

- **ToF measurement:** The [VL53L1X datasheet](https://www.st.com/resource/en/datasheet/vl53l1x.pdf) specifies distance modes, timing budgets, and range limits.

- **ROS 2 range data:** The [sensor_msgs/Range message definition](https://github.com/ros2/common_interfaces/blob/jazzy/sensor_msgs/msg/Range.msg) describes fields and validity rules used by the listener.

- **Virtual device:** [Duckiematrix setup](https://docs.duckietown.com/ente/duckietown-manual/50-duckiematrix/getting-started/duckiematrix-first-steps.html) covers preparing the simulated sensors.

## For LX authors

Learner material is in `notebooks/` and `packages/`; checkpoint prompts and model answers are in
`checkpoint_data/`, and structural and subscriber checks are in `tests/`. Run checks from the LX root:

```bash
python3 -m pytest tests/
ruff check .
```
