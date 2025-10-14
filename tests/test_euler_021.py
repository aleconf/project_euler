#!/usr/bin/env python

from src.euler_021 import solver


def test_answer():
    """See https://oeis.org/A259180"""
    assert solver(10000) == sum(
        [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368]
    )
