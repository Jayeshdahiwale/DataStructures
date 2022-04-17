"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Append a list

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def append_list(list_first,list_second):
    """
    Description : It appends list second to list first
    :param list_first:Takes a first list as input
    :param list_second: Takes a second list as input
    :return: Returns an ppended list
    """
    try:
        if list_first.__class__.__name__ != "list" or list_second.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes  both parameters as a list")
        sys.exit()
    total_list = list_first + list_second
    return total_list



if __name__ == "__main__":
    list1 = [1, 3, 5, 7, 9]
    list2 = [1, 2, 4, 6, 7, 8]
    logging.info(list1)
    logging.info(list2)
    logging.info(f"The appended list is : {append_list(list1,list2)}")
