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
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])

def iterate_dic(dictionary):
    """
    Description : This function iterates over the dictionary to show key and values
    :param dictionary: It takes dictionary as an input
    :return: It doesn't return anything
    """
    for key,value in dictionary.items():
        logging.info(f"{key} corresponds to {value}")

if __name__=="__main__":
    d = {'Red': 1, 'Green': 2, 'Blue': 3}
    iterate_dic(d)
