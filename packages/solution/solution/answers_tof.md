# Duckiedrone ToF LX: theory answers

> Answers to the questions each notebook opens with.

## Notebook 1: time-of-flight sensors, the basics

1. What does a time-of-flight sensor measure, and how does the VL53L1X turn detected light into a
   distance?

2. Why does the distance reported by a stationary sensor change from one reading to the next?

3. Why is the maximum range not a fixed number, and what sets it?

4. Why do the errors of a rangefinder not accumulate the way the errors of an integrated
   acceleration do?

## Notebook 2: the Duckiedrone ToF data flow

1. Which pieces of software handle a range reading between the chip and a subscriber?

2. What does each one add to, or remove from, the reading?

3. What sets how often a new reading arrives?

4. Why do a target the sensor cannot detect and a target beyond $3.6\,\mathrm{m}$ arrive on the topic as the
   same value?

5. Why does stopping the learner subscriber not stop the flight-control path, while a ToF driver or
   bridge failure stops both?

## Notebook 3: subscribing to the ToF topic

1. Which program publishes the downward ToF topic, and which programs subscribe to it?

2. How often does the downward ToF topic publish, and how can that be checked?

3. What does one printed line describe?

4. Which printed values are not distances, and what should a consumer do with them?

## Notebook 4: using all five sensors

1. What has to be running on the Duckiedrone before a topic exists to subscribe to?

2. Where do the five topic names come from, and why can they be generated rather than listed?

3. Why do the five readings in one printed line come from different measurement times?
