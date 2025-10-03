#!/usr/bin/env python

from src.euler_009 import solver


def test_answer():
    assert solver(12) == 60
