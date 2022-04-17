"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Replace all occurrences of  first char with $
"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def char_frequency(string):
    """
    Description: This function calculates the frequency of characters in a string
    :param string: This takes string as an input
    :return:It returns a dictionary where key as char value as frequency
    """
    try:
        if string.__class__.__name__ != "str":
            raise TypeError
    except TypeError:
        logging.error("Function only takes string as an argument")
        sys.exit()

    first_char = string[0]
    string = list(string)
    for i in range(1,len(string)):
        if  string[i] == first_char:
            string[i]= "$"
    string ="".join(string)
    return string


if __name__ == "__main__":
    string = input("Enter any string :").lower()
    logging.info(char_frequency(string))
