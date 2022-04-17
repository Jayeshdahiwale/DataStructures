"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Length of String
"""
import logging
import sys


logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])
def len_string(string):
    """
    Description: This function calculates the length of a string
    :param string: This takes string as an input
    :return: function returns the length of a string
    """
    try:
        if string.__class__.__name__ != "str":
            raise TypeError
    except TypeError:
        logging.error("Function only takes string as an argument")
        sys.exit()
    return len(string)

if __name__ == "__main__":
    string = input("Write something :")
    logging.info(len_string(string))


