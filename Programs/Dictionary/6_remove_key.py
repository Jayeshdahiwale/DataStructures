"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Removing a key from dictionary

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def remove_key(dictionary):
    """
    Description: This function removes the key from function if exists
    :param dictionary: It takes the dictionary as param to show user keys,values they want to del
    :return: It returns the updated dictionary
    """

    logging.info(dictionary)
    choice = input("Please input which key you want to delete : ")
    if choice in dictionary:
        del dictionary[choice]
        return dictionary
    else:
        logging.info("Key not exist")


if __name__ == "__main__":
    myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    logging.info(remove_key(myDict))
