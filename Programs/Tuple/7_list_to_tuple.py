"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Convert list to tuple
"""
import logging
import sys


logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("../sample.log"), logging.StreamHandler(sys.stdout)])


def convert_list_tuple(list_):
    """
    Description :This function convert list into tuple
    :param: It takes a list as a param
    :return: It returns a tuple back
    """
    try:
        if list_.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.info("function takes only list as a param")
        sys.exit()
    logging.info(f"The original list is {list_} ")
    logging.info(f"The converted tuple is {tuple(list_)} ")
    return tuple(list_)


if __name__ == "__main__":
    list_ =[1,2,3,True,"Jayesh",1,2,4]
    logging.info(convert_list_tuple(list_))