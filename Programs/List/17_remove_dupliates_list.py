"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Remove duplicates from a list of list

"""
import logging
import sys
import itertools

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def remove_duplicate_list(list_of_list):
    """
    Description :Function removes the duplicates' list from a list
    :param list_input:Takes a list of list as input
    :return: returns an updated list
    """
    try:
        if list_input.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes  list as a param")
        sys.exit()
    list_of_list.sort()
    new_list = list(list_of_list for list_of_list, _ in itertools.groupby(list_of_list))
    return new_list


if __name__ == "__main__":
    list_input = [[10, 20], [40], [30, 56, 25], [10,20], [33], [40]]
    logging.info(f"The list is {list_input}")
    logging.info(f"The list after removing duplicates is : {remove_duplicate_list(list_input)}")
