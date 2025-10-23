#!/usr/bin/env python


def solver(n: int) -> int:
    """Main solver of the task."""
    return len(set([a**b for a in range(2, n + 1) for b in range(2, n + 1)]))


def main() -> None:
    """Print the solution."""
    print(solver(100))


if __name__ == "__main__":
    main()
