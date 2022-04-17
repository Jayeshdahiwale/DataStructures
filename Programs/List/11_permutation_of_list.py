"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Permutation of List

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def list_permutation(list_first):
    """
    Description : It performs permuation on list
    :param list_first:Takes a first list as input
    :return: Returns a list with permutation
    """
    try:
        if list_first.__class__.__name__ != "list":
            raise TypeError
    except TypeError:
        logging.error("Function takes  both parameters as a list")
        sys.exit()
    if len(list_first) == 0:
        return []
    if len(list_first) == 1:
        return [list_first]
    l = []
    for i in range(len(list_first)):
        m = [list_first[i]]
        rem_lst = list_first[:i]+list_first[i+1:]
        for p in list_permutation(rem_lst):
            l.append((m + p))

    return l



if __name__ == "__main__":
    data = list("123")
    logging.info(data)
    logging.info(f"The list output permutation : {list_permutation(data)}")
