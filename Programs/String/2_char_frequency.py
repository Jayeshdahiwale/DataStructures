"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Frequency of Characters
"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def char_frequency(string):
    """
    Description: This function calculates the frequency of characters in a string
    :param string: This takes string as an input
    :return:It returns a dictionary where key as char value as frequency
    """
    try:
        if string.__class__.__name__ != "str":
            raise TypeError
    except TypeError:
        logging.error("Function only takes string as an argument")
        sys.exit()

    d = dict()
    for n in string:
        if n in d.keys():
            d[n] += 1
        else:
            d[n] = 1
    return d


if __name__ == "__main__":
    string = input("Enter any string :")
    logging.info(char_frequency(string))
