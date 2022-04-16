"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Lowers the first n characters of the string
"""
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def lower_first_n_char(string_,a):
    """
    Description: this function returns the uppercse nd lowercase of the word
    :param string_: This takes  string as a parameter
    :param a :  is the number of first letters we want to lowercase
    :return:It returns a string
    """
    try:
        if string_.__class__.__name__ != "str" or a.__class__.__name__!= "int":
            raise TypeError
    except TypeError:
        logging.error("Function  string as 1st argument and int as second argument")
        sys.exit()
    if len(string_) >= a:
        string_ =string_[:a].lower()+ string_[a:]
        return string_

    else:
        try:
            raise IndexError
        except IndexError:
            logging.info(IndexError("Index out of range"))



if __name__ == "__main__":
   word = "JAYESH"
   logging.info(lower_first_n_char(word,3))



