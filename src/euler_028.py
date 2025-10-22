#!/usr/bin/env python


def compute_corners_sum(n: int) -> int:
    """Sum the four corners of the n-spiral/square."""
    return 4 * (n**2) - 6 * (n - 1)


def solver(n: int) -> int:
    """Main solver of the task.

    The spiral always form a square of side n.
    I n is odd the spiral ends in the top right corner,
    whereas f n is even it ends in the bottom left corner.
    Either way the values in the four corners are:
    n^2, n^2-(n-1),n^2-2(n-1), n^2-3(n-1).
    """

    if n % 2 == 0:
        starting = 2
        result = 0
    else:
        starting = 3
        result = 1
    for i in range(starting, n + 1, 2):
        result += compute_corners_sum(i)
    return result


def main() -> None:
    """Print the solution."""
    print(solver(1001))


if __name__ == "__main__":
    main()
