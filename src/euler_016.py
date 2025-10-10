#!/usr/bin/env python


def solver(n: int) -> int:
    """Main solver of the task."""
    return sum([int(x) for x in str(int("1" + "0" * n, 2))])


def main() -> None:
    """Print the solution."""
    print(solver(1000))


if __name__ == "__main__":
    main()
