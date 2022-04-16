"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Generate Array

"""
import random
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def gen_array():
    """"
    Description : This function generates the array of 5 random integers
    Parameters : It takes no parameters
    Return : Function doesn't return anything
    """
    rand_array = []
    for i in range(5):
        rand_array.append(random.randint(0, 100))

    for i in range(len(rand_array)):
        logging.info(rand_array[i])


if __name__ == "__main__":
    gen_array()
