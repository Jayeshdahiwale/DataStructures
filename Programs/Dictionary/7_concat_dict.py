"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Concat the dictionaries
"""

import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample1.log"), logging.StreamHandler(sys.stdout)])


def concat_dict(dict_list):
    """
     Description: It takes the list of dictionaries and concatenate them
    :param dict_list: It takes the list of dictionaries
    :return: It returns the concatenated dictionaries
    """
    dic = {}
    for d in dict_list: dic.update(d)
    return dic


if __name__ == "__main__":
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 2: 60}
    logging.info(concat_dict([dic1, dic2, dic3]))
