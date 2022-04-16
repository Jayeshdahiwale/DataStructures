"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Returns the upper and lower case of a string
"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def string_cases(string_):
    """
    Description: this function returns the uppercse nd lowercase of the word
    :param string_: This takes  string as a parameter
    :return:It returns a tuple containing _>(upper, lower)
    """
    try:
        if string_.__class__.__name__ != "str":
            raise TypeError
    except TypeError:
        logging.error("Function only takes string as an argument")
        sys.exit()
    return string_.upper(), string_.lower()


if __name__ == "__main__":
   word = "jayesH"
   upper,lower = string_cases(word)
   logging.info(upper)
   logging.info(lower)



