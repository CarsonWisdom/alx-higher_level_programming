#!/usr/bin/python3


def safe_print_division(a, b):
    """
    divides two integers and prints the result
    """
    try:
        res = a / b
    except:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
