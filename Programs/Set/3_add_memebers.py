"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Add elements in a set

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def add_members(set_, list_):
    """
    Description : Add elements to the existing set
    :param set_:Takes a set where we want to add the elements
    :param list_: Takes elements in the format of list
    :return: returns the updates set
    """
    try:
        if set_.__class__.__name__ != "set" or list_.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes set as 1st param, and list as second param")
        sys.exit()
    temp = [set_.add(i) for i in list_]
    return set_


if __name__ =="__main__":
    set_ = {1,2,3,4}
    elements = [5,6,7]
    logging.info(add_members(set_,elements))