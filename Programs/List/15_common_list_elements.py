"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : It gives a list consist of common elements from two list

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def common_element_list(list_first,list_second):
    """
    Description : It finds the common elements between two list
    :param list_first:Takes a first list as input
    :param list_second: Takes a second list as input
    :return: Returns a list with common elements
    """
    try:
        if list_first.__class__.__name__ != "list" or list_second.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes  both parameters as a list")
        sys.exit()
    return list(set(list_first) & set(list_second))




if __name__ == "__main__":
    list1 = [10, 10, 0, 0, 10]
    list2 = [10, 10, 10, 0, 0]
    logging.info(list1)
    logging.info(list2)
    logging.info(f"The list with common elements : {common_element_list(list1,list2)}")
