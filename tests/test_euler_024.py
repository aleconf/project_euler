#!/usr/bin/env python

from src.euler_024 import solver


def test_answer():
    input_string = ["0", "1", "2"]
    assert solver(input_string, 5) == "201"
