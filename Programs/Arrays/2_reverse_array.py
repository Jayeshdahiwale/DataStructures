"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Reverse Array

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def rev_array(arr):
    """"
        Description : It takes the list as input and returns reverse list
        Parameters : It takes the list as input
        Return : It returns the reversed list
        """
    rev_arr = []
    for i in reversed(arr):
        rev_arr.append(i)
    return rev_arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    logging.info(rev_array(arr))
