"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Finding longest word from the list
"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def longest_string(list_):
    """
    Description: this function finds the longest word in a list of string
    :param list_: This takes a list as a parameter
    :return:It returns a string
    """
    try:
        if list_.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function only takes string as an argument")
        sys.exit()
    longest_word = ""
    for word in list_:
        if len(longest_word)<len(word):
            longest_word = word
    return longest_word


if __name__ == "__main__":
   words = ["Jayesh","Prakash","aa","bba"]
   logging.info(longest_string(words))



