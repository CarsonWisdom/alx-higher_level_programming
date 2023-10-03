#!/usr/bin/python3
# 9-print_last_digit.py


def print_last_digit(number):
    """Printing last digit of a number - return it."""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
