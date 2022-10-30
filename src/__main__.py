#
# Вводим английское слово, а он тебе пример.
# License: GPL v3
# from .wooordhunt import wooordhunt_parser
import argparse
import tkinter as tk

class AppInterface(tk.Tk):
    pass


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("word", type=str)
    argument_parser.add_argument("-i", "--interface", action="store_true")
    argument_parser.add_argument("-t", "--test", action="store_true")
    args = argument_parser.parse_args(["fire", "-i"])

    if args.interface:
        pass

    if args.test:
        pass
    else:
        pass
