"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Iterate over set

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])

def set_iterate(set_):
    """
    Description: This function iterate over a set
    :param set_: It takes a parameter as a set
    :return: it doesn't return anything
    """
    try:
        if set_.__class__.__name__ != "set":
            raise TypeError()
    except TypeError:
        logging.error(TypeError("This function only takes set as a parameter"))
        sys.exit()
    for element in set_:
        logging.info(element)

if __name__=="__main__":
    elements = input("Enter the elements for a set :").split(",")
    set_iterate(set(elements))

