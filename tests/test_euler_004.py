#!/usr/bin/env python

from src.euler_004 import solver


def test_answer():
    assert solver(2) == 9009
