"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Convert dictionary into table

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def dict_to_table(dictionary):
    """
    Description: This function converts dictionary into table
    :param dictionary: It takes dictionary as an input
    :return: It doesn't return anything
    """
    for row in zip(*([key] + value for key, value in sorted(dictionary.items()))):
        logging.info(" ".join([str(i) for i in row]))


if __name__=="__main__":
    my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}
    dict_to_table(my_dict)
