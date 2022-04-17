"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Check Multiple Keys

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample1.log"), logging.StreamHandler(sys.stdout)])


def check_multi_keys(dictionary):
    """
    Description : This function checks whether multiple keys exists in a dict or not
    :param dictionary: It takes dictionary as an input
    :return: it returns the boolean value
    """
    try:
        if dictionary.__class__.__name__ != "dict":
            raise TypeError("Function takes only dictionary as argument")
    except TypeError:
        return logging.error(TypeError)
    if len(dictionary) > 1:
        return True
    return False


if __name__ =="__main__":
    d = {1:"Red",2:"Blue"}
    logging.info(check_multi_keys(d))