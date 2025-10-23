#!/usr/bin/env python


def upper_bound_digits(n: int) -> int:
    """Find an upper bound on the number of digits for candidates numbers."""
    i = 1
    while i * (9**n) >= 10 ** (i - 1):
        i += 1
    return i - 1


def solver(n: int) -> int:
    """Main solver of the task."""
    result = 0
    for i in range(2, 10 ** upper_bound_digits(n)):
        aux = 0
        for digit in str(i):
            aux += int(digit) ** n
        if i == aux:
            result += i
    return result


def main() -> None:
    """Print the solution."""
    print(solver(5))


if __name__ == "__main__":
    main()
