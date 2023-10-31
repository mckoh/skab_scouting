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

    """This class lets you prepare the data of the SKAB dataset for
    machine learning. You can use this class to load the data from directory,
    prepare them and split them

    :param data_directory: The directory to load the csv data from
    """

    def __init__(self, data_directory):
        self._data = data = load_data_from_dir(
            dir_name=data_directory,
            sep=";",
            parse_dates=[0],
            index_col=0
        )

        self._X, self._y = None, None
        self._X_snips, self._y_snips = None, None
        self.__split_vertically()

    def __split_vertically(self, x_cols=X_COLUMNS, y_cols=Y_COLUMNS):
        """Lets you select the columns that are used as machine learning input

        :param x_cols: A list of column names
        :param y_cols: A list of column names
        :return: None
        """
        self._X = self._data[x_cols]
        self._y = self._data[y_cols]

    def __split_horizontally(self, window_size=10, shift=10):
        """Lets you split the DataFrame into snippets of some size

        :param window_size: The number of time steps to include in snippet
        :param shift: The number of time steps to shift the window
        :return: None
        """

        xv = self._X.values
        yv = self._y.values

        a_snips = []
        b_snips = []

        for i in range(0, len(a)-window_size, shift):
            self._X_snips.append(xv[i:i+window_size])
            self._y_snips.append(yv[i+window_size])

    def split_data(self, x_cols=X_COLUMNS, y_cols=Y_COLUMNS, window_size=10, shift=10):
        self.__split_vertically(x_cols, y_cols)
        self.__split_horizontally(window_size, shift)