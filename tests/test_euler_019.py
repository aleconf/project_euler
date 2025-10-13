#!/usr/bin/env python

from src.euler_019 import solver


def test_answer():
    assert solver(1900, 1901, 1, "Monday") == 4
