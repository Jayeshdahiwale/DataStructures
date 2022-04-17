"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Remove element from a tuple
"""
import logging
import sys


logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("../sample.log"), logging.StreamHandler(sys.stdout)])


def remove_element(tuple_,element):
    """
    Description :This function removes element from a tuple
    :param: It takes a tuple as a param
    :param: It takes an element to be removed as a param
    :return: It return an updated tuple
    """
    try:
        if tuple_.__class__.__name__ != "tuple":
            raise TypeError
    except TypeError:
        logging.info("function takes only list as a param")
        sys.exit()
    tuple_ = list(tuple_)
    if element in tuple_:
        tuple_.remove(element)
        logging.info("Element removed successfully")
        return tuple(tuple_)
    logging.info("Element not found in tuple")
    return tuple(tuple_)




if __name__ == "__main__":
    tuple_ = (1,2,3,4,5,6,7)
    element = 7
    logging.info(remove_element(tuple_,element))