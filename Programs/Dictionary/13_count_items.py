"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Counts Items In Dictionary

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])

def count_items(dictionary):
    """
    Description : This function counts the number of items in dictionary
    :param dictionary:
    :return: Returns the number of items
    """
    try:
        if dictionary.__class__.__name__ != "dict":
            raise TypeError("Function takes only dictionary as argument")
    except TypeError:
        logging.error(TypeError)
        sys.exit()
    return sum(map(len, dictionary.values()))

if __name__ =="__main__":
    d = {1:[2,3,4],2:[5,6,7],3:[8,9,10]}
    logging.info(count_items(d))