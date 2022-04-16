"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Multiplies elements of list

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def multiplies_elements(list_input,multiplier):
    """
    Description :Function multiplies every element of a list
    :param list_input:Takes a list as input
    :param multiplier:multiplier will multiply every element of list
    :return: returns a updated list
    """
    try:
        if list_input.__class__.__name__ != "list" or multiplier.__class__.__name__ != "int":
            raise TypeError
    except TypeError:
        logging.error("Function takes  list as a first param and int as a second param")
        sys.exit()
    list_input = list(map(lambda x: x * multiplier,list_input))
    return list_input


if __name__ =="__main__":
    list_input = [1,2,3,4,5,6,7]
    logging.info(f"The list is {list_input}")
    multiplier = int(input("Enter the multiplier in integer format :"))
    logging.info(multiplies_elements(list_input,multiplier))