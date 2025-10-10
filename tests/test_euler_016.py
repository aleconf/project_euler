#!/usr/bin/env python

from src.euler_016 import solver


def test_answer():
    assert solver(15) == 26
