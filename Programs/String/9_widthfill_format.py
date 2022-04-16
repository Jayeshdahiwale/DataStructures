"""
@Author: Jayesh Dahiwale
@Date: 2022-04-13 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-13 18:00:30
@Title : Fill the width format of string
"""
import logging
import sys
import textwrap

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


def string_widthfill(string_):
    """
    Description: this function sets the widthformat of string to 50
    :param string_: This takes  a string or pra whose with to be set
    :return:It returns a string
    """
    try:
        if string_.__class__.__name__ != "str" :
            raise TypeError
    except TypeError:
        logging.error("Function takes string as rgument")
        sys.exit()
    return textwrap.fill(string_, width=50)



if __name__ == "__main__":
   para = "JAYESHESH svvej dve errv erv wv erv wdv scwev wefw ewvwe wevwevwew wevwev wevwevwever  erbe  sdvw r e"
   logging.info(string_widthfill(para))