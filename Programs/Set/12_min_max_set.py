"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Min Max Elements in a set

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def min_max(set_):
    """
    Description: This function find the minimum and max element in a set
    :param set_: take set_ as  a parameter
    :return: It returns the tuple containing two element 0 th inedx min 1 st index max
    """
    try:
        if set_.__class__.__name__ != "set":
            raise TypeError
    except TypeError:
        logging.error("Function takes param as set")
        sys.exit()
    result = min(list(set_)), max(list(set_))
    return result

if __name__ == "__main__":
    set = {"a","b","c","d"}
    logging.info(min_max(set))
