#!/usr/bin/env python

from src.euler_008 import solver


def test_answer():
    with open("data/input_project_euler_008.txt", "r") as file:
        content = file.read()
    loaded_input = "".join(content.splitlines())
    assert solver(loaded_input, 4) == 5832
