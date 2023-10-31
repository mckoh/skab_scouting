"""
SKAB PREPARATION ENGINE
Author: Michael Kohlegger
Date: October 2023
"""


from numpy import array, append
from .functions import load_data_from_dir


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
        self._X_snips, self._y_snips = [], []
        self._window_size = None
        self._shift = None

    def __split_vertically(self, x_cols, y_cols):
        """Lets you select the columns that are used as machine learning input

        :param x_cols: A list of column names
        :param y_cols: A list of column names
        :return: None
        """
        self._X = self._data[x_cols]
        self._y = self._data[y_cols]

    def __split_horizontally(self, window_size, shift):
        """Lets you split the DataFrame into snippets of some size

        :param window_size: The number of time steps to include in snippet
        :param shift: The number of time steps to shift the window
        :return: None
        """

        # Create some temporary files
        xv = self._X.values
        yv = self._y.values

        self._window_size = window_size
        self._shift = shift

        for i in range(0, len(xv)-window_size, shift):
            self._X_snips.append(xv[i:i+window_size])
            self._y_snips.append(yv[i+window_size])

        self._X_snips = array(self._X_snips)
        self._y_snips = array(self._y_snips)

    def split_data(self, x_cols=X_COLUMNS, y_cols=Y_COLUMNS, window_size=10, shift=1):
        """Lets you perform a vertical and a horizontal split in one go

        This function is necessary, as it is common to first do a vertical
        and only then a horizontal split in your data.

        :param x_cols: A list of column names
        :param y_cols: A list of column names
        :param window_size: The number of time steps to include in snippet
        :param shift: The number of time steps to shift the window
        :return: None
        """

        self.__split_vertically(x_cols, y_cols)
        self.__split_horizontally(window_size, shift)

    # GETTER FUNCTIONS

    def get_data(self, return_xy=False):
        """Lets you return your data.

        :param return_xy: If true, method returns data as x an y
        :return: Data as pandas.DataFrame
        """
        if return_xy:
            return self._X, self._y
        return self._data

    def get_snippets(self):
        """Lets you return your data as time snippets.

        :return: Data as numpy.array
        """
        return self._X_snips, self._y_snips

    def get_ts_params(self):
        """Lets you return the construction parameters of your ts snips.

        :return: parameters as tuple (window size, shift)
        """
        return self._window_size, self._shift

    def get_snips_shape(self):
        """Lets you return the shape of your snippets data.

        :return: Shapes as tuple (X.shape, y.shape)
        """
        return self._X_snips.shape, self._y_snips.shape

    #TODO: Data Visualization
