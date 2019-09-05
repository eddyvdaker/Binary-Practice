#!/usr/bin/env python
"""
    Binary_Practice.questions
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Functions for generating questions.

    :copyright: 2019 Eddy van den Aker (eddy.v.d.aker@gmail.com,
        eddy.vandenaker@zuyd.nl)
    :license: MIT
"""
from random import getrandbits
from typing import Union

from binary_practice.conversions import to_binary
from binary_practice.generators import generate_number

# Question Types
ANY_QUESTION = 'any'
DECIMAL_TO_BINARY = 'decimal to binary'
BINARY_TO_DECIMAL = 'binary to decimal'

question_types = [ANY_QUESTION, DECIMAL_TO_BINARY, BINARY_TO_DECIMAL]


class Question(object):
    """A question object represents a question, including the original
    number, the answers, and the question text to show the user.
    """

    def __init__(self, number: Union[int, str], answer: Union[int, str], 
            text: str):
        """Initiate the Question object.

        :param number: The original number
        :param answer: The answer to the question
        :param text: The question text to show the user
        """
        self.number = number
        self.answer = answer
        self.text = text
    
    def render_question(self) -> str:
        """Renders the question for the user.

        :return: the rendered question text
        """
        return f'{self.text}:'
    
    def check_answer(self, user_answer: str) -> bool:
        """Checks the user's input against the answer.

        :param user_answer: The user's input
        :return: Whether the user's input matches the answer or not
        """
        return str(user_answer) == str(self.answer)


def get_question(question_type: str=ANY_QUESTION) -> Question:
    """Get a question of the specified type, which by default is any
    type of question.

    :param question_type: The type of question
    :return: A Question object or None
    """
    if question_type == ANY_QUESTION:
        if getrandbits(1):              # if a 1 is returned
            return get_binary_to_decimal_question()
        else:                           # if a 0 is returned
            return get_decimal_to_binary_question()
    elif question_type == DECIMAL_TO_BINARY:
        return get_decimal_to_binary_question()
    elif question_type == BINARY_TO_DECIMAL:
        return get_binary_to_decimal_question()


def get_decimal_to_binary_question() -> Question:
    """Get a decimal to binary question.

    :return: a Question object
    """
    number = generate_number()
    return Question(number, to_binary(number), f'Convert {number} to binary')


def get_binary_to_decimal_question() -> Question:
    """Get a binary to decimal question.

    :return: a Question object
    """
    answer = generate_number()
    number = to_binary(answer)
    return Question(number, answer, f'Convert {number} to decimal')
