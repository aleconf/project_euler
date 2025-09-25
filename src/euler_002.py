#!/usr/bin/env python


def solver(upper_bound: int) -> int:
    """Solver of the task.

    The recursive formula for even valued Fibonacci numbers is used.
    """

    a = 2
    b = 8
    total = 10
    while True:
        aux = a + (4 * b)
        a = b
        b = aux
        if b > upper_bound:
            break
        total += b
    return total


def main() -> None:
    """Print the solution."""
    print(solver(4000000))


if __name__ == "__main__":
    main()
