"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : FrozenSet Use

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])
def frozen_set_implement():
    """
    description : It is just an implementation of Frozenset
    param : It takes not params
    :return: It returns nothing
    """
    x = frozenset([1, 2, 3, 4, 5])
    y = frozenset([3, 4, 5, 6, 7])
    # use isdisjoint(). Return True if the set has no elements in common with other.
    logging.info(x.isdisjoint(y))
    # use difference(). Return a new set with elements in the set that are not in the others.
    logging.info(x.difference(y))
    # new set with elements from both x and y
    logging.info(x | y)


if __name__=="__main__":
    frozen_set_implement()