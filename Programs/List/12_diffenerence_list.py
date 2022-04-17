"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Difference of list

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def list_difference(list_first,list_second):
    """
    Description : It calculates the difference between two sets
    :param list_first:Takes a first list as input
    :param list_second: Takes a second list as input
    :return: Returns a list with differences
    """
    try:
        if list_first.__class__.__name__ != "list" or list_second.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes  both parameters as a list")
        sys.exit()

    diff_list1_list2 = list(set(list_first) - set(list_second))
    diff_list2_list1 = list(set(list_second) - set(list_first))
    total_diff = diff_list1_list2 + diff_list2_list1
    return total_diff



if __name__ == "__main__":
    list1 = [1, 3, 5, 7, 9]
    list2 = [1, 2, 4, 6, 7, 8]
    logging.info(list1)
    logging.info(list2)
    logging.info(f"The difference between list : {list_difference(list1,list2)}")
