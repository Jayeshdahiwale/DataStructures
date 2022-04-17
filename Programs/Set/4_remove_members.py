"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Remove elements in a set

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def remove_members(set_, list_):
    """
    Description : Remove elements from the existing set
    :param set_:Takes a set from where we want to remove the elements
    :param list_: Takes elements in the format of list
    :return: returns the updated set
    """
    try:
        if set_.__class__.__name__ != "set" or list_.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes set as 1st param, and list as second param")
        sys.exit()
    for i in list_:
        try:
            set_.remove(i)
        except KeyError:
            logging.error(f"{i} is not found in set")
    return set_

if __name__ =="__main__":
    set_ = {1,2,3,4}
    elements = [1,2,3]
    logging.info(remove_members(set_,elements))