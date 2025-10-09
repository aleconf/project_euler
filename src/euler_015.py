#!/usr/bin/env python


import math


def solver(n: int, m: int) -> int:
    """Main solver of the task."""
    return math.comb(n + m, n)


def main() -> None:
    """Print the solution."""
    print(solver(20, 20))


if __name__ == "__main__":
    main()
