from random import choice
from re import sub

from sympy import latex


def different(i, options):
    d = None
    while d is None or d == i:
        d = choice(options)
    return d


def clean(ltx):
    # '+/- -' to '-/+'
    if not isinstance(ltx, str):
        ltx = latex(ltx)
    ltx = sub(r'\+\s?-', '-', ltx)
    ltx = sub(r'-\s?-', '+', ltx)
    # refactor Sympy's strange infinity LaTeX
    ltx = sub(r'\\tilde\\{\\infty\\}', r'\\infty', ltx)
    return ltx


def int_range(start, stop, skip = (0,)):
    return [n for n in range(start, stop) if not skip or n not in skip]
