"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Find the smallest element in a list

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def smallest_elements(list_input):
    """
    Description :Function finds the smallest element
    :param list_input:Takes a list of int, float as input
    :return: returns a smaleest element
    """
    try:
        if list_input.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes  list as a param")
        sys.exit()
    min_element = min(list_input)
    return min_element


if __name__ =="__main__":
    list_input = [1,2,3,4,5,6,7]
    logging.info(f"The list is {list_input}")
    logging.info(f"The smallest element is : {smallest_elements(list_input)}")