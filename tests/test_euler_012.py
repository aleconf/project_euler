#!/usr/bin/env python

from src.euler_012 import solver


def test_answer():
    assert solver(5) == 28
