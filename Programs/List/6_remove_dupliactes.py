"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Remove duplicates from a list

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def remove_duplicates(list_input):
    """
    Description :Function removes the duplicates' element from a list
    :param list_input:Takes a list as input
    :return: returns an updated string
    """
    try:
        if list_input.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes  list as a param")
        sys.exit()
    return list(set(list_input))


if __name__ == "__main__":
    list_input = input("Enter any values separated by comma :").split(",")
    logging.info(f"The list is {list_input}")
    logging.info(f"The list after removing duplicates is : {remove_duplicates(list_input)}")
