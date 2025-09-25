#!/usr/bin/env python

from src.euler_001 import solver


def test_answer():
    assert solver(3, 5, 9) == 23
