#!/usr/bin/env python

from src.euler_007 import solver


def test_answer():
    assert solver(6) == 13
