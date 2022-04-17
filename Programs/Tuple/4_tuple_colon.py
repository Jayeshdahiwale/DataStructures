"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Make a tuple colon
"""
import logging
import sys
from copy import deepcopy


logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def tuple_colon():
    """
    Description :This function makes a colon of tuple
    :return: It doesn't return anything
    """
    # create a tuple
    tuplex = ("HELLO", 5, [], True)
    logging.info("Original tuple")
    logging.info(tuplex)
    # make a copy of a tuple using deepcopy() function
    tuplex_colon = deepcopy(tuplex)
    tuplex_colon[2].append(50)
    logging.info("Colon tuple print")
    logging.info(tuplex_colon)

if __name__ =="__main__":
    tuple_colon()


