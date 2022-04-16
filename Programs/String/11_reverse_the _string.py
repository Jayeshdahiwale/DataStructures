"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Lowers the first n characters of the string
"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def reverse_string(string_):
    """
    Description: this function reverse the string
    :param string_: This takes  string  to be reversed as a parameter
    :return:It returns a reversed string
    """
    try:
        if string_.__class__.__name__ != "str":
            raise TypeError
    except TypeError:
        logging.error("Function  string as 1st argument and int as second argument")
        sys.exit()
    return "".join(list(reversed(string_)))



if __name__ == "__main__":
   word = "JAYESH"
   logging.info(reverse_string(word))



