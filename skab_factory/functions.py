"""
SKAB FACTORY
Author: Michael Kohlegger
Date: October 2023
"""

from pandas import read_csv
from pandas import concat
from os import listdir
from os.path import join


def load_data_from_dir(dir_name, allowed_extension="csv", *args, **kwargs):
    """This function will load data from multiple csv files in a data dir.

    Besides dir_name, you can pass arguments and keyword arguments to
    the pandas.read_csv function, by adding them to this function's
    parameter list. The function will always return a pandas.DataFrame.
    To succeed, you need to make sure that the schema of all contained
    csv files is equal (i.e. all must have the same columns in the same
    order).

    The function will add an additional column to the pandas.DataFrame
    containing the name of the file, the respective row has been loaded
    from. The column is called "origin" (e.g. "1.csv")

    :param dir_name: The directory name to load from
    :return: pandas.DataFrame with data
    """
    first = True
    for file in listdir(dir_name):
        if file[-3:] == allowed_extension:
            temp_file_path = join(dir_name, file)
            if first:
                data = read_csv(temp_file_path, *args, **kwargs)
                data["origin"] = str(temp_file_path)
            else:
                temp_data = read_csv(temp_file_path, *args, **kwargs)
                temp_data["origin"] = str(temp_file_path)
                data = concat([data, temp_data])
            first = False
    return data.sort_index()