"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Occurences of specific element

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])

def occurence(arr, element):
    """
    Description : It tells the specified occurence of an element in  given array
    Parameter : it takes array and element as a parameter
    Returns : It returns the number of time an element repeat
    """
    times = 0
    for i in arr:
        if i == element:
            times += 1
    return times


if __name__ == "__main__":
    arr = [1, 2, 1, 4, 1]
    element = 1
    logging.info(occurence(arr, element))
