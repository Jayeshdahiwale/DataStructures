"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Slice operation on tuple
"""
import logging
import sys


logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("../sample.log"), logging.StreamHandler(sys.stdout)])


def slice_tuple():
    """
    Description :This function implements operations on tuple
    :param : It doesn't take any parameter
    :return: it doesn't return anything
    """
    # create a tuple
    tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
    # used tuple[start:stop] the start index is inclusive and the stop index
    _slice = tuplex[3:5]

    logging.info(_slice)
    # if the start index isn't defined, is taken from the beg inning of the tuple
    _slice = tuplex[:6]
    logging.info(_slice)
    # if the end index isn't defined, is taken until the end of the tuple
    _slice = tuplex[5:]
    logging.info(_slice)
    # if neither is defined, returns the full tuple
    _slice = tuplex[:]
    logging.info(_slice)
    # The indexes can be defined with negative values
    _slice = tuplex[-8:-4]
    logging.info(_slice)

if __name__ == "__main__":
    slice_tuple()