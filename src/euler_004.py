#!/usr/bin/env python


def solver(n: int) -> int:
    """Main solver of the task."""
    min_range = int("1" + (n - 1) * "0")
    max_range = int(n * "9")
    result = 0

    for i in range(min_range, max_range + 1):
        for j in range(min_range, max_range + 1):
            candidate = i * j
            candidate_str = str(candidate)
            if candidate_str == candidate_str[::-1] and result < candidate:
                result = candidate
    return result


def main() -> None:
    """Print the solution."""
    print(solver(3))


if __name__ == "__main__":
    main()
