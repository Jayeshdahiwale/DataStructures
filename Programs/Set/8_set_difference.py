"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Difference of Sets

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])

def set_difference(set_1,set_2):
    """
    Description: This function takes the difference
    :param set_1: It represents the first set
    :param set_2: It represents the second set
    :return: Returns difference of sets-> Basically the updated set_1
    """
    try:
        if set_1.__class__.__name__ != "set" or set_2.__class__.__name__ != "set":
            raise TypeError
    except TypeError:
        logging.error("Function takes both param as set")
        sys.exit()
    temp = [set_1.remove(i) for i in set_2 if i in set_1]
    return set_1

if __name__ =="__main__":
    set_1 = {1, 2, 3, 4, 5}
    set_2 = {2, 7, 8, 9, 10, 3}
    logging.info(set_difference(set_1, set_2))