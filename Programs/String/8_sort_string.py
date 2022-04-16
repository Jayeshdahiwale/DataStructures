"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Sort the words in list alphanumeriiclly
"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def string_sort(list_):
    """
    Description: This function sorts the list of words alphanumerically
    :param list_: This takes  list of words as a parameter
    :return:It returns a list with sorted words nd unique one
    """
    try:
        if list_.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function only takes string as an argument")
        sys.exit()
    words =[word.lower() for word in list_]
    words.sort()
    return words


if __name__ == "__main__":
   string_ = input("Enter the words separeted by comma").split(",")
   logging.info(string_sort(string_))



