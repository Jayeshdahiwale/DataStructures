"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Sum of elements in a list

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def sum_elements(list_input):
    """
    Description :Function calculates the sum of elements
    :param list_input:Takes a list as input
    :return: returns sum of element
    """
    try:
        if list_input.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes only list as a param")
        sys.exit()
    try:
        for i in list_input:
            if i.__class__.__name__ != "int":
                if i.__class__.__name__ != "float":
                    raise TypeError
    except TypeError:
        logging.info("You should either insert integer or float")
        sys.exit()
    return sum(list_input)


if __name__ =="__main__":
    list_input = [float(i) for i in input("enter the values separated by comma :").split(",")]
    logging.info(sum_elements(list_input))