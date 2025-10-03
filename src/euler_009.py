#!/usr/bin/env python


def solver(n: int) -> int | str:
    """Main solver of the task.

    a**2 + (n-a-c)**2 - c**2 == 0
    Computing c from it, we get
    c == (2 * a**2 + n**2 - 2 * n * a) / (2 * (n - a))
    """

    for a in range(1, n - 2):
        i = 2 * a**2 + n**2 - 2 * n * a
        j = 2 * (n - a)
        if i % j == 0:
            c = int(i / j)
            return a * c * (n - a - c)
    return "No solution"


def main() -> None:
    """Print the solution."""
    print(solver(1000))


if __name__ == "__main__":
    main()
