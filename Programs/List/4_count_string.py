"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Count Strings in a list

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def count_string(list_input):
    """
    Description :Count string with length >2 and first char = second char
    :param list_input:Takes a list of string as input
    :return: returns a count  of specific strings
    """
    try:
        if list_input.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes  list as a param")
        sys.exit()
    list_output = [string for string in list_input if len(string) > 2 and string[0] == string[-1]]
    return len(list_output)


if __name__ == "__main__":
    list_input = input("Enter the different words separated with comma :").split(",")
    logging.info(f"The list is {list_input}")
    logging.info(f"The list output is : {count_string(list_input)}")
