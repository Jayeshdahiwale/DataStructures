"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Clear the set

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def clear_set(set_1):
    """
    Description: This function clears the existing set
    :param set_1: It represents the  set to be clear
    :return: Returns empty set
    """
    try:
        if set_1.__class__.__name__ != "set":
            raise TypeError
    except TypeError:
        logging.error("Function takes both param as set")
        sys.exit()
    set_1 = {}
    return set_1

if __name__ == "__main__":
    set_1 = {1, 2, 3, 4, 5}
    logging.info("Original Sets")
    logging.info(set_1)
    logging.info("final set")
    logging.info(clear_set(set_1))
