# Duckiedrone ToF LX: theory answers

> Answers to the questions each notebook opens with.

## [Time-of-Flight (ToF) Sensor Fundamentals](../../../notebooks/1-tof-basics.ipynb)

1. How does a rangefinder work, and in particular, how does the VL53L1X use light to estimate distance?

2. Why do repeated measurements vary when the Duckiedrone remains stationary?

3. How do the target, ambient light, and measurement settings affect usable range?

4. Why does a direct range measurement behave differently from a position estimate obtained by integrating acceleration?

## [Measuring ToF sensor accuracy](../../../notebooks/2-measuring-tof-sensor-accuracy.ipynb)

1. How close is the average reported distance to an independently measured reference?

2. How do the mean, median, and standard deviation help describe the result?

3. How might target material, distance, sensor choice, or driver settings affect it?

## [Duckiedrone ToF Sensor Architecture](../../../notebooks/3-duckiedrone-tof-architecture.ipynb)

1. How does a reading travel from a ToF sensor to a ROS 2 subscriber?

2. Which component determines its units, timestamp, and range limits?

3. How does the same sensor supply information to the flight controller?

4. What constrains the publication rate, and how are configuration changes applied?

## [Subscribing to the ToF sensor data](../../../notebooks/4-subscribing-to-tof.ipynb)

1. How does a subscriber receive and store a ToF reading?

2. How can the input rate and display rate be observed separately?

3. What information is retained from each message?

4. How should reported values and continued message arrival be checked?

## [All Five Sensors](../../../notebooks/5-all-five-sensors.ipynb)

1. Which services supply the four additional sensor streams?

2. How does one subscriber associate each message with its sensor?

3. What does a line containing five ranges reveal about the surrounding scene?

4. How can the timing of those readings affect their interpretation?
