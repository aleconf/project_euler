#!/usr/bin/env python

from src.euler_005 import lcm, solver


def test_answer():
    assert lcm(4, 6) == 12
    assert solver(10) == 2520
