#!/usr/bin/env python


def solver(n: int) -> int:
    """Main solver of the task.

    From https://docs.python.org/3/c-api/long.html#integer-objects
    > All integers are implemented as “long” integer objects of arbitrary size.
    Therefore it is better to work just with integers instead of using Binet
    formula or computation by rounding.
    """

    previous = 0
    actual = 1
    index = 1
    while True:
        if actual >= 10 ** (n - 1):
            return index
        else:
            previous, actual = actual, actual + previous
            index += 1


def main() -> None:
    """Print the solution."""
    print(solver(1000))


if __name__ == "__main__":
    main()
