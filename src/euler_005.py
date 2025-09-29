#!/usr/bin/env python

from functools import reduce
import math


def lcm(a: int, b: int) -> int:
    """Compute the lcm of two numbers."""
    return int(a * b / math.gcd(a, b))


def solver(n: int) -> int:
    """Main solver of the task."""
    return reduce(lcm, [x for x in range(1, n + 1)])


def main() -> None:
    """Print the solution."""
    print(solver(20))


if __name__ == "__main__":
    main()
