# SKAB Scouting

SKAB is a benchmark dataset for anomaly detection in timeseries data. This repo contains the SKAB dataset along with some scouting notebooks. SKAB uses a simple experimental setup to generate timeseries data with anomalies (see setup below).

![SKAB test setup](static/testbed.png)

The following items are located on the image above. The number in brackets shows the amount of contained units per item.

* **1, 2:** solenoid valve (1)
* **3:** a tank with water (1)
* **4:** a water pump (1)
* **5:** emergency stop button (1)
* **6:** electric motor (1)
* **7:** inverter (1)
* **8:** compactRIO (1)
* **9:** a mechanical lever for shaft misalignment (1)
* **Not shown parts:** vibration sensor (2), pressure meter (1), flow meter (1), thermocouple (2)

## Notebooks

There are several scouting notebooks contained:

* **`notebooks/loading_data_other.ipynb`:** This notebook contains some usefull functions that can be used to load multiple SKAB files from a single data directory (e.g. `data/other`).
* ...

## SKAB Data Description

These are the columns that the SKAB dataset contains for all experiments

* **`datetime`:** Represents dates and times of the moment when the value is written to the database (YYYY-MM-DD hh:mm:ss)
* **`Accelerometer1RMS`:** Shows a vibration acceleration (Amount of g units)
* **`Accelerometer2RMS`:** Shows a vibration acceleration (Amount of g units)
* **`Current`:** Shows the amperage on the electric motor (Ampere)
* **`Pressure`:** Represents the pressure in the loop after the water pump (Bar)
* **`Temperature`:** Shows the temperature of the engine body (The degree Celsius)
* **`Thermocouple`:** Represents the temperature of the fluid in the circulation loop (The degree Celsius)
* **`Voltage`:** Shows the voltage on the electric motor (Volt)
* **`RateRMS`:** Represents the circulation flow rate of the fluid inside the loop (Liter per minute)
* **`anomaly`:** Shows if the point is anomalous (0 or 1)
* **`changepoint`:** Shows if the point is a changepoint for collective anomalies (0 or 1)

## References

* [SKAB Dataset on Github](https://github.com/waico/SKAB)
