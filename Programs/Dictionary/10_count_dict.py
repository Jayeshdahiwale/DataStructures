"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Count the dictionary with specific value

"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample1.log"), logging.StreamHandler(sys.stdout)])


def count_dict(list_dict, key):
    """
    Descritpion: This function count the dictionaries in list which have some value
    :param key: This key is searched in the every dictionary
    :param list_dict: This is a list containing dictionaries
    :return: It returns the total count
    """
    try:
        if list_dict.__class__.__name__ != "list":
            raise TypeError("Function takes a list as first argument and int or boolean as second arg")
    except TypeError:
        logging.info(TypeError)
        sys.exit()
    try:
        return sum(d[key] for d in list_dict)
    except Exception:
        logging.info(Exception("Only works with the keys having boolean or int value"))
        sys.exit()


if __name__ == "__main__":
    list_dict = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'},
                 {'id': 3, 'success': True, 'name': 'Alex'}]
    key = "id"
    logging.info(f"The total count is {count_dict(list_dict, key)}")
