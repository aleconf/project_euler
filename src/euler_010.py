#!/usr/bin/env python


def prime_sieve(n: int) -> set[int]:
    """Find all primes <= N using the sieve of Eratosthenes."""
    primes = [1 for _ in range(n + 1)]
    for i in range(4, n + 1, 2):
        primes[i] = 0
    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i] == 1:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    result = set()
    for i in range(2, n + 1):
        if primes[i] == 1:
            result.add(i)
    return result


def solver(n: int) -> int:
    """Main solver of the task."""
    return sum(prime_sieve(n))


def main() -> None:
    """Print the solution."""
    print(solver(2000000))


if __name__ == "__main__":
    main()
