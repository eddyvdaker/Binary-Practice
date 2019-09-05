#!/usr/bin/env python
"""
    Binary_Practice.cli
    ~~~~~~~~~~~~~~~~~~~

    Command-line interface for the application.

    :copyright: 2019 Eddy van den Aker (eddy.v.d.aker@gmail.com,
        eddy.vandenaker@zuyd.nl)
    :license: MIT
"""
from binary_practice.questions import ANY_QUESTION, BINARY_TO_DECIMAL, \
    DECIMAL_TO_BINARY, get_question

def menu():
    print("### Binary Practice ###")
    while True:
        print("--- Menu ---")
        print("[1] Practice binary to decimal")
        print("[2] Pracitce decimal to binary")
        print("[3] Practice both binary to decimal and decimal to binary")
        print("[q] Quit")
        choice = input('Please choose what you want to pracice: ')
        if choice == '1':
            practice(question_type=BINARY_TO_DECIMAL)
        elif choice == '2':
            practice(question_type=DECIMAL_TO_BINARY)
        elif choice == '3':
            practice()
        elif choice.lower() == 'q':
            quit(0)
        else:
            print('Invalid option, please choose again.')


def practice(question_type=ANY_QUESTION):
    keep_practicing = True
    while keep_practicing:
        print()
        question = get_question(question_type=question_type)
        answer = input(question.render_question())
        if question.check_answer(answer):
            print('Correct!')
        else:
            print(f'Incorrect, the correct answer was {question.answer}.')
        answer = input('Keep practicing [Y/n]: ')
        if answer.lower() == 'n':
            keep_practicing = False


if __name__ == '__main__':
    menu()
