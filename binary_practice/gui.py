#!/usr/bin/env python
"""
    Binary_Practice.gui
    ~~~~~~~~~~~~~~~~~~~

    Graphical interface for the application.

    :copyright: 2019 Eddy van den Aker (eddy.v.d.aker@gmail.com,
        eddy.vandenaker@zuyd.nl)
    :license: MIT

    :TODO: room for a lot of improvement in the GUI code
"""
import tkinter as tk

from binary_practice.questions import ANY_QUESTION, BINARY_TO_DECIMAL, \
    DECIMAL_TO_BINARY, get_question


class QuestionFrame(tk.Frame):

    def __init__(self, master=None, app=None, question_type=ANY_QUESTION):
        super().__init__(master)
        self.master = master
        self.app = app

        # Get first question
        self.question_type = question_type
        self.question = get_question(question_type=question_type)

        # Setup question label
        self.question_label = tk.Label(self)
        self.question_label['text'] = str(self.question.number)
        self.question_label.pack()

        # Setup answer box
        self.answer_box = tk.Text(self, width=30, height=1)
        self.answer_box.pack()

        self.sep1 = tk.Label(self)
        self.sep1.pack()

        # Setup check button
        self.check_button = tk.Button(self)
        self.check_button['text'] = 'Check answer'
        self.check_button['command'] = self.check_answer
        self.check_button.pack()

        self.sep2 = tk.Label(self)
        self.sep2.pack()

        # Setup check label
        self.check_label = tk.Label(self)
        self.check_label['text'] = ''
        self.check_label.pack()

        self.sep3 = tk.Label(self, height=2)
        self.sep3.pack()

        # Setup next button
        self.next_button = tk.Button(self)
        self.next_button['text'] = 'Next question'
        self.next_button['command'] = self.next_question
        self.next_button.pack()
        
        self.sep4 = tk.Label(self)
        self.sep4.pack()

        # Setup menu button
        self.menu_button = tk.Button(self)
        self.menu_button['text'] = 'Go back to menu'
        self.menu_button['command'] = self.app.hide_question
        self.menu_button.pack()

    def next_question(self):
        self.question_type = self.app.question_type
        self.question = get_question(question_type=self.question_type)
        self.question_label['text'] = str(self.question.number)
        self.answer_box.delete(1.0, tk.END)
        self.check_label['text'] = ''

    def check_answer(self):
        answer = self.answer_box.get(1.0, tk.END).rstrip()
        if self.question.check_answer(answer):
            self.check_label['text'] = 'Correct!'
        else:
            self.check_label['text'] = 'Incorrect, the correct answer was ' \
                f'{self.question.answer}.'


class MenuFrame(tk.Frame):

    def __init__(self, master=None, app=None):
        super().__init__(master)
        self.master = master
        self.app = app

        # Button Binary to Decimal
        self.b2d = tk.Button(self)
        self.b2d['text'] = 'Practice binary to decimal'
        self.b2d.pack(side='top')
        self.b2d['command'] = self.set_question_type_b2d

        # Button Decimal to Binary
        self.d2b = tk.Button(self)
        self.d2b['text'] = 'Practice decimal to binary'
        self.d2b.pack(side='top')
        self.d2b['command'] = self.set_question_type_d2b

        # Button Binary to Decimal and Decimal to Binary
        self.any = tk.Button(self)
        self.any['text'] = 'Practice both binary to decimal and decimal to ' \
            'binary'
        self.any.pack(side='top')
        self.any['command'] = self.set_question_type_any
    
    def set_question_type_any(self):
        self.app.set_question_type(ANY_QUESTION)
        self.app.hide_menu()

    def set_question_type_b2d(self):
        self.app.set_question_type(BINARY_TO_DECIMAL)
        self.app.hide_menu()

    def set_question_type_d2b(self):
        self.app.set_question_type(DECIMAL_TO_BINARY)
        self.app.hide_menu()


class Application(tk.Frame):

    def __init__(self):
        super().__init__()
        self.question_type = ANY_QUESTION

        self.separator = tk.Frame(height=1, bd=1, relief=tk.SUNKEN)
        self.separator.pack(fill=tk.X, padx=5, pady=5)

        self.menu_frame = MenuFrame(master=self.master, app=self)
        self.menu_frame.pack()

        self.question_frame = QuestionFrame(master=self.master, app=self)

    def set_question_type(self, question_type):
        self.question_type = question_type

    def hide_menu(self):
        self.menu_frame.pack_forget()
        self.question_frame.next_question()
        self.show_question()

    def show_menu(self):
        self.menu_frame.pack()

    def hide_question(self):
        self.question_frame.pack_forget()
        self.show_menu()

    def show_question(self):
        self.question_frame.pack()


def gui_factory():
    root = tk.Tk()
    root.geometry('400x300')
    root.resizable(width=False, height=False)
    root.title('Binary Practice')
    app = Application()
    return app
