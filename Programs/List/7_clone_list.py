"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Clones the list

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def clones_list(list_input):
    """
    Description :Function clones or copy the provided list
    :param list_input:Takes a list as input
    :return: returns a cloned list
    """
    try:
        if list_input.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes  list as a param")
        sys.exit()
    cloned_list = list(list_input)
    return cloned_list


if __name__ == "__main__":
    list_input = input("Enter any values separated by comma :").split(",")
    logging.info(f"The list is {list_input}")
    logging.info(f"The clone_list : {clones_list(list_input)}")
