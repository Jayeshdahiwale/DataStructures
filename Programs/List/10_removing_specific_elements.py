"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Removing specific elements

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def remove_specific_element(list_first):
    """
    Description : Tells whether the two list have common elements or not
    :param list_first:Takes a first list as input
    :return: returns a boolean value whether the list have something in common
    """
    try:
        if list_first.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes  both parameters as a list")
        sys.exit()
    if len(list_first) < 6 :
        logging.info("Input a list with 6 or more elements")
    else:
        list_output = list_first[1:3]+list_first[5:]
        return list_output



if __name__ == "__main__":
    list_first = input("Enter the different words separated with comma :").split(",")
    logging.info(list_first)
    logging.info(f"The list output : {remove_specific_element(list_first)}")
