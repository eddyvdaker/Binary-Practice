#!/usr/bin/env python
"""
    Binary_Practice.conversions
    ~~~~~~~~~~~~~~~

    A simple application to help students practice binary to decimal
    and decimal to binary conversions.

    :copyright: 2019 Eddy van den Aker (eddy.v.d.aker@gmail.com,
        eddy.vandenaker@zuyd.nl)
    :license: MIT
"""
from binary_practice.cli import menu
from binary_practice.gui import gui_factory

def start_cli():
    menu()

def start_gui():
    gui_factory().mainloop()
