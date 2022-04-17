"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : dding key to dict

"""
import logging
import sys


logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample1.log"), logging.StreamHandler(sys.stdout)])


def add_key(dictionary, key, value):
    """
    Description: This function adds new key to the element or can update the existing key
    :param value: It takes value to be added with corresponding key
    :param key: It takes a key to be added to dictionary
    :param dictionary: It takes a dictionary as a input
    :return: returns the updated dictionary
    """
    dictionary.update({key: value})
    logging.info("The updated dictionary is :")
    return dictionary


if __name__ == "__main__":
    key = 2
    value = "Red"
    dictionary = {2: "Blue", 3: "White"}
    logging.info(add_key(dictionary, key, value))
