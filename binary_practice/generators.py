#!/usr/bin/env python
"""
    Binary_Practice.generators
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Functions for the random generation of numbers.

    :copyright: 2019 Eddy van den Aker (eddy.v.d.aker@gmail.com,
        eddy.vandenaker@zuyd.nl)
    :license: MIT
"""
from random import randint
from typing import List


def generate_number(min: int=0, max: int=255, ignore: List[int]=[]) -> int:
    """Generates a random number between the min and max values 
    specified (defaults to 8-bit unsigned numbers).

    :param min: The lower limit of the random generated number
    :param max: The upper limit of the random generated number
    :param ignore: A list of numbers to ignore
    :return: The random generated number 
    """
    while True:
        number = randint(min, max)
        if number not in ignore:
            return number

