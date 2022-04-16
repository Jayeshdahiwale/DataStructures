"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Unpack a Tuple with diff data types
"""
import logging
import random
import sys
import string

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def unpack_tuple(tuple_):
    """
    Description :This function unpacks tuple into different variable
    :param: It takes a tuple as a parameter
    :return: It doesn't return anything
    """
    try:
        if tuple_.__class__.__name__ != "tuple":
            raise TypeError
    except TypeError:
        logging.info("function takes only tuple as a param")
        sys.exit()
    for i in tuple_:
        logging.info(i)


if __name__ == "__main__":
    tuple_ =(1,2,3,True,"Jayesh")
    unpack_tuple(tuple_)
