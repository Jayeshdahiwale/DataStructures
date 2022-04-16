"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Reverse touple
"""
import logging
import sys


logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def reverse_tuple(tuple_):
    """
    Description :This function reverse the tuple
    :param: It takes a tuple as a parameter
    :return: It returns a reversed tuple
    """
    try:
        if tuple_.__class__.__name__ != "tuple":
            raise TypeError
    except TypeError:
        logging.info("function takes only tuple as a param")
        sys.exit()
    tuple_ = reversed(list(tuple_))
    return tuple(tuple_)

if __name__ == "__main__":
    tuple_ =(1,2,3,True,"Jayesh",1,2,4)
    logging.info(reverse_tuple(tuple_))

