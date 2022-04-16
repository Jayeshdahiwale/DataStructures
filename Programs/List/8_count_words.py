"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Count words  in a list whose length is greater than given num

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def list_words(list_input, number):
    """
    Description :Count string with length >2 and first char = second char
    :param list_input:Takes a list of string as input
    :param number: Takes a number for which the length will be compared
    :return: returns an updated list
    """
    try:
        if list_input.__class__.__name__ != "list" or number.__class__.__name__ != "int":
            raise TypeError
    except TypeError:
        logging.error("Function takes  list as a param")
        sys.exit()
    list_output = [word for word in list_input if len(word) > number ]
    return list_output


if __name__ == "__main__":
    list_input = input("Enter the different words separated with comma :").split(",")
    number = int(input("Enter the number :"))
    logging.info(f"The list is {list_input}")
    logging.info(f"The list output is : {list_words(list_input,number)}")
