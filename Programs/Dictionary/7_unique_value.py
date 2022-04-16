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

def unique_values(list_dict):
    """
    Description:It returns a unique values from dictionary
    :param: This function take list of dictionaries as a parameter
    :return: It returns a set of unique values
    """
    logging.info(list_dict)
    unique_values = set(values for dic in list_dict for values in dic.values())
    logging.info("The unique values are :")
    return unique_values

if __name__ == "__main__":
    list_dict =[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    logging.info(unique_values(list_dict))