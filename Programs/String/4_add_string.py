"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Add ly, ing to the string
"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def add_string(string):
    """
    Description: This function add ing at the end or ly if ing in the end
    :param string: This takes string as an input
    :return:It returns a string
    """
    try:
        if string.__class__.__name__ != "str":
            raise TypeError
    except TypeError:
        logging.error("Function only takes string as an argument")
        sys.exit()
    if len(string) < 3:
        return string
    elif string[-3:] == "ing":
        return string + "ly"
    else:
        return string + "ing"


if __name__ == "__main__":
    string = input("Enter the string :")
    logging.info(add_string(string))
