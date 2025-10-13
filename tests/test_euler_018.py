#!/usr/bin/env python

from src.euler_018 import solver


input1 = """3
7 4
2 4 6
8 5 9 3"""


def test_answer():
    assert solver(input1) == 23
