"""
SKAB PREPARATION ENGINE
Author: Michael Kohlegger
Date: October 2023
"""


from functions import load_data_from_dir

X_COLUMNS = [
    "Accelerometer1RMS",
    "Accelerometer2RMS",
    "Current",
    "Pressure",
    "Temperature",
    "Thermocouple",
    "Voltage",
    "Volume Flow RateRMS"
]

Y_COLUMNS = [
    "anomaly"
]


class PreparationEngine:

    def __init__(self, data_directory):
        self._data = data = load_data_from_dir(
            dir_name=data_directory,
            sep=";",
            parse_dates=[0],
            index_col=0
        )

        self._X, self._y = None, None
        self.__split_vertically()

    def __split_vertically(self):
        self._X = self._data[X_COLUMNS]
        self._y = self._data[Y_COLUMNS]

    def __split_horizontally(self):
        pass