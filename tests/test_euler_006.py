#!/usr/bin/env python

from src.euler_006 import sum_of_squares, square_of_sum, solver


def test_answer():
    assert sum_of_squares(10) == 385
    assert square_of_sum(10) == 3025
    assert solver(10) == 2640
