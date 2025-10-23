#!/usr/bin/env python

from src.euler_029 import solver


def test_answer():
    assert solver(5) == 15
