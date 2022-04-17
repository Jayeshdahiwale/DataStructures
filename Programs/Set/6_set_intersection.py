"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Intersection of Sets

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])

def set_intersection(set_1,set_2):
    """
    Description: This function takes the intersection
    :param set_1: It represent the first set
    :param set_2: It represents the second set
    :return: Returns common intersected set
    """
    try:
        if set_1.__class__.__name__ != "set" or set_2.__class__.__name__ != "set":
            raise TypeError
    except TypeError:
        logging.error("Function takes both param as set")
        sys.exit()
    intersected_set = set([i for i in set_1 if i in set_2])
    return intersected_set

if __name__ == "__main__":
    set_1 = {1,2,3,4,5}
    set_2 ={2,7,8,9,10,3}
    logging.info(set_intersection(set_1,set_2))