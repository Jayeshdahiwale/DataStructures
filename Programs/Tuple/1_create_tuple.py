"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Create a Tuple
"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def create_tuple():
    """
     Description: It creates a  tuple by asking values from the user
     param: Function takes no parameter
    :return: Function returns a tuple
    """
    elements = input("Enter the values separated by comma to make the tuple :").split(",")
    return tuple(elements)


if __name__ == "__main__":
    logging.info(create_tuple())
