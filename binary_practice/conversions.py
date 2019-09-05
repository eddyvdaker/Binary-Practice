#!/usr/bin/env python
"""
    Binary_Practice.conversions
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Functions for the conversion from decimal to binary.

    :copyright: 2019 Eddy van den Aker (eddy.v.d.aker@gmail.com,
        eddy.vandenaker@zuyd.nl)
    :license: MIT
"""


def to_binary(number: int) -> str:
    """Convert a decimal number to a binary numbers.
    
    :param number: The number to convert to binary
    :return: The binary representation of the number
    """
    return bin(number)[2:]   # First 2 characters are for signed/unsigned