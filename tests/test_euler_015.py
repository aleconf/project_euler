#!/usr/bin/env python

from src.euler_015 import solver


def test_answer():
    assert solver(2, 2) == 6
