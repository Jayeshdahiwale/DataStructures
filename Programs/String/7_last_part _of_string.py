
"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Print the string character before a specified lst character
"""
import logging
import sys


logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def string_cut_char(string_,char_):
    """
    Description:  get the last part of a string before a specified character.
    :param string_: This takes  a string from where the lst part is taken
    :param char_: the char_ is used to find it in the string
    :return:It returns a string
    """
    try:
        if string_.__class__.__name__ != "str" or char_.__class__.__name__ != "str":
            raise TypeError
    except TypeError:
        logging.error("Function takes both argument as string")
        sys.exit()
    return string_.rsplit(char_, 1)[0]



if __name__ == "__main__":
   string_ = "https://www.w3resource.com/python-exercises/string"
   logging.info(string_cut_char(string_,"/"))