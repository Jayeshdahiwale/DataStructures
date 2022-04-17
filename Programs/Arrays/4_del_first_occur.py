"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Delete First Occurence

"""
import sys
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def del_first_occur(arr, ele):
    """
    Description: This function deletes the first occurence of a provided element
    :param arr: It takes array as an parameter
    :param ele: It takes an element whose occurence to be removed
    :return: It returns either the processed list or return a string
    """
    for i in arr:
        if i == ele:
            arr.remove(i)
            return f"The resulted array is :{arr}"
    else:
        return f"Element not found in given array"


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 4, 4]
    ele = 4
    logging.info(del_first_occur(arr, ele))
