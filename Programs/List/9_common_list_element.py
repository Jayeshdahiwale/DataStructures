"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Tells whether the two list have common elements or not

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def list_common_element(list_first, list_second):
    """
    Description : Tells whether the two list have common elements or not
    :param list_first:Takes a first list as input
    :param list_second: Takes a second list as input
    :return: returns a boolean value whether the list have something in common
    """
    try:
        if list_first.__class__.__name__ != "list" or list_second.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes  both parameters as a list")
        sys.exit()
    return len(set(list_first).intersection(set(list_second))) >= 1



if __name__ == "__main__":
    list_first = input("Enter the different words separated with comma :").split(",")
    list_two =  input("Enter the different words separated with comma :").split(",")
    logging.info(f"The two have at least a common element : {list_common_element(list_first,list_two)}")
