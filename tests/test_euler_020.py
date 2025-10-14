#!/usr/bin/env python

from src.euler_020 import solver


def test_answer():
    assert solver(10) == 27
