"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Union of Sets

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])

def set_union(set_1,set_2):
    """
    Description: This function takes the union
    :param set_1: It represents the first set
    :param set_2: It represents the second set
    :return: Returns union set
    """
    try:
        if set_1.__class__.__name__ != "set" or set_2.__class__.__name__ != "set":
            raise TypeError
    except TypeError:
        logging.error("Function takes both param as set")
        sys.exit()
    list_1 = list(set_1)
    temp = [list_1.append(i) for i in set_2]

    return set(list_1)

if __name__ == "__main__":
    set_1 = {1,2,3,4,5}
    set_2 ={2,7,8,9,10,3}
    logging.info(set_union(set_1,set_2))