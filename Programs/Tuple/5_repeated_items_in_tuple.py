"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Repeated items in tuple
"""
import logging
import sys


logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def repeted_item(tuple_):
    """
    Description :This function shows element which are repeating
    :param: It takes a tuple as a parameter
    :return: It returns a set of element which are repeted
    """
    try:
        if tuple_.__class__.__name__ != "tuple":
            raise TypeError
    except TypeError:
        logging.info("function takes only tuple as a param")
        sys.exit()
    d =set()
    for i in tuple_:
        if tuple_.count(i) > 1:
            d.add(i)
    return d

if __name__ == "__main__":
    tuple_ =(1,2,3,True,"Jayesh",1,2,4)
    logging.info(repeted_item(tuple_))

