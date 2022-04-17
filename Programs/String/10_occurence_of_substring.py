"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Count the occurrence of substring
"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def count_occurrence(string_,sub_string):
    """
    Description: this function count the no of occurrence of substring in the string
    :param string_: This takes  string  from where no of sub_string to be counted
    :param sub_string: This string is used to find it's occurence
    :return:It returns a count of occurence
    """
    try:
        if string_.__class__.__name__ != "str" or sub_string.__class__.__name__ != "str":
            raise TypeError
    except TypeError:
        logging.error("Function takes string as 1st and 2nd argument")
        sys.exit()
    return string_.count(sub_string)



if __name__ == "__main__":
   word = "JAYESHESH"
   sub_word = "ESH"
   logging.info(count_occurrence(word,sub_word))