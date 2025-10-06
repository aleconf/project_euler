#!/usr/bin/env python

import math


def divisors(n: int) -> int:
    """Compute the numbers of divisors."""
    result = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result += 2
    if n == int(math.sqrt(n)) ** 2:
        result -= 1
    return result


def solver(n: int) -> int:
    """Main solver of the task."""
    i = 1
    while True:
        if i % 2 == 0:
            a = int(i / 2)
            b = i + 1
        else:
            a = int((i + 1) / 2)
            b = i
        if divisors(a) * divisors(b) > n:
            return int(i * (i + 1) / 2)
        else:
            i += 1


def main() -> None:
    """Print the solution."""
    print(solver(500))


if __name__ == "__main__":
    main()
