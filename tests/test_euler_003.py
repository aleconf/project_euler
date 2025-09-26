#!/usr/bin/env python

from src.euler_003 import smallest_prime_factor, solver


def test_answer():
    assert smallest_prime_factor(13195) == 5
    assert solver(13195) == 29
