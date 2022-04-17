"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Splits list on the basis of first character

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def split_first_char(user_input):
    """
    Description : It Splits list on the basis of first character
    :param user_input:Takes a user_input as a string
    :return: Returns a list
    """
    try:
        if user_input.__class__.__name__ != "str":
            raise TypeError
    except TypeError:
        logging.error("Function takes only string as a parameter")
        sys.exit()
    return user_input.split(f"{user_input[0]}")




if __name__ == "__main__":
    user_input = input("Enter any word or sentence :")
    logging.info(f"The splitter list is  : {split_first_char(user_input)}")
