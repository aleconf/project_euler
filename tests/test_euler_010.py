#!/usr/bin/env python

from src.euler_010 import solver


def test_answer():
    assert solver(10) == 17
