#!/usr/bin/env python

from src.euler_017 import solver


def test_answer():
    assert solver(5) == 19
