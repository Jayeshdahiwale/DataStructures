"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Sort list on the basis of last element of tuple

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])

def last(n):return n[-1]
def sort_list(list_input):
    """
    Description :Sort the list of tuple on the basis of their last elements
    :param list_input:Takes a list of tuple as input
    :return: returns a count  of specific strings
    """
    try:
        if list_input.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes  list as a param")
        sys.exit()
    return sorted(list_input, key=last)


if __name__ == "__main__":
    list_input = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    logging.info(f"The list is {list_input}")
    logging.info(f"The list output is : {sort_list(list_input)}")
