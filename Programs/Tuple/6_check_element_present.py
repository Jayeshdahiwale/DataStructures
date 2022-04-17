"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Check Element present in a tuple
"""
import logging
import sys


logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def check_element_present(tuple_,element):
    """
    Description :This function checks whether element present or not
    :param: It takes a tuple as a parameter
    :param: it takes eleement to be find as a param
    :return: It returns boolean value
    """
    try:
        if tuple_.__class__.__name__ != "tuple":
            raise TypeError
    except TypeError:
        logging.info("function takes only tuple as a param")
        sys.exit()
    d =set()
    if element in tuple_:
        logging.info("Element present in tuple")
        return True
    logging.info("Element not present in table")
    return False

if __name__ == "__main__":
    tuple_ =(1,2,3,True,"Jayesh",1,2,4)
    element = 7
    logging.info(check_element_present(tuple_,element))

