#!/usr/bin/env python


def sum_of_squares(n: int) -> int:
    """Compute the square of the sum of all numbers up to n."""
    return int(n * (n + 1) * ((2 * n) + 1) / 6)


def square_of_sum(n: int) -> int:
    """Compute the sum of squares for all numbers up to n."""
    sum_formula = int(n * (n + 1) / 2)
    return pow(sum_formula, 2)


def solver(n: int) -> int:
    """Main solver of the task."""
    return abs(sum_of_squares(n) - square_of_sum(n))


def main() -> None:
    """Print the solution."""
    print(solver(100))


if __name__ == "__main__":
    main()
