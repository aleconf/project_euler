#!/usr/bin/env python


def number_sum(n: float) -> int:
    """Compute the sum of all positive integers up to n."""
    m = int(n)
    return int(m * (m + 1) / 2)


def solver(p: int, q: int, n: int) -> int:
    """Main solver of the task: both p and q must be prime numbers."""
    return int(
        (p * number_sum(n / p))
        + (q * number_sum(n / q))
        - (p * q * number_sum(n / (p * q)))
    )


def main() -> None:
    """Print the solution."""
    print(solver(3, 5, 999))


if __name__ == "__main__":
    main()
