"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Sorting the dictionary

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample1.log"), logging.StreamHandler(sys.stdout)])


def sort_dict(dictionary, reverse=False):
    """
    Description: this function sorts the dictionary by value
    :param reverse: Reverse parameter has set with false default value.. It will be used for reverse sorting
    :param dictionary: It takes dictionary as a parameter with key value entries
    :return: It returns the sorted dictionary as per the choice of user
    """
    if not reverse:
        return f"The sorted dictionary in ascending order {dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=reverse))}"
    else:
        return f"The sorted dictionary in descending order {dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=reverse))} "


if __name__ == "__main__":
    d = {"Red": 5, "Black": 3, "Blue": 4, "Green": 8}
    logging.info(sort_dict(d))
