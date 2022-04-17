"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Generating a dictionary with key:key^2

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample1.log"), logging.StreamHandler(sys.stdout)])


def generate_dic():
    """
    Description : This function generates a dictionary with key 1 to n and value = key^2
    :return: it returns the dictionary
    """
    d = dict()
    try:
        num = int(input("Enter the number positive integer number"))
    except Exception:
        logging.error(Exception("Enter valid key"))
        return generate_dic()
    for i in range(1, num + 1): d.update({i: i * i})
    return d

if __name__=="__main__":
    logging.info(generate_dic())
