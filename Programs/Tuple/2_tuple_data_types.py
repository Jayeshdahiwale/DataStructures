"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Create a Tuple with diff data types
"""
import logging
import random
import sys


logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def tuple_diff_data_types():
    """
    Description :This function just implements a creation of tuple with diff data types
    :return: It returns a tuple with different datatypes
    """
    list_ = ["tuple", False, 3.2, 1]
    tuple_ = tuple(random.sample(list_,random.randint(1,4)))
    return tuple_

if __name__=="__main__":
    logging.info(tuple_diff_data_types())