"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : remove item from set

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def remove_item(set_, item):
    """
    Description : Remove item from set if present
    :param item: it take the item to be remove from set if present
    :param set_:Takes a set from where we want to remove the item if present
    :return: returns the updated set
    """
    try:
        if set_.__class__.__name__ != "set":
            raise TypeError
    except TypeError:
        logging.error("Function takes set as 1st param")
        sys.exit()
    if item in set_:
        set_.remove(item)
        logging.info("Removed successfully")

    return set_

if __name__ =="__main__":
    set_ = {1,2,3,4}
    item = 1
    logging.info(remove_item(set_,item))