"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Nested dictionary with keys

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample1.log"), logging.StreamHandler(sys.stdout)])

def nested_dict(list):
    """
    Description: It converts list to the nested dictionaries
    :param list: It takes a list as argument
    :return: it returns a dictionary
    """
    new_dict = current = {}
    for name in list:
        current[name] = {}
        current = current[name]
    return new_dict

if __name__ == "__main__":
    list = [1,2,3,4]
    logging.info(nested_dict(list))