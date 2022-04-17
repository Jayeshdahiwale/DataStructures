"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Convert string into dictionary

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample1.log"), logging.StreamHandler(sys.stdout)])


def string_to_dict(string):
    """
    Description:This function takes the string and converts each letter to key and their occurrence to value
    :param string:
    :return: It returns the dictionary
    """
    my_dict = {}
    for letter in string:
        my_dict[letter] = my_dict.get(letter, 0) + 1
    return my_dict

if __name__=="__main__":
    string = input("Enter the string :")
    logging.info(string_to_dict(string.lower()))