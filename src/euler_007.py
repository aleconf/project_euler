#!/usr/bin/env python


import math


def prime_sieve(n: int) -> list[int]:
    """Find all primes <= N using the sieve of Eratosthenes."""
    primes = [1 for _ in range(n + 1)]
    for i in range(4, n + 1, 2):
        primes[i] = 0
    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i] == 1:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    result = list()
    for i in range(2, n + 1):
        if primes[i] == 1:
            result.append(i)
    return result


def solver(m: int) -> int:
    """Main solver of the task.

    It uses a result cited in https://arxiv.org/abs/1002.0442
    """

    log1 = math.log(m)
    log2 = math.log(log1)
    upper_limit = max(
        int(m * (log1 + log2 - 1 + ((log2 - 2) / (log1)))) + 1, 688383
    )

    primes = prime_sieve(upper_limit)
    return primes[m - 1]


def main() -> None:
    """Print the solution."""
    print(solver(10001))


if __name__ == "__main__":
    main()
