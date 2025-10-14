#!/usr/bin/env python


def solver(n: int) -> int:
    """Main solver of the task."""
    sum_proper_divisors = [0 for _ in range(n)]
    for i in range(1, n):
        for j in range(i * 2, n, i):
            sum_proper_divisors[j] += i
    result = 0
    to_skip = dict()
    for i in range(1, n):
        if i in to_skip:
            continue
        aux = sum_proper_divisors[i]
        if aux < n and sum_proper_divisors[aux] == i and aux != i:
            result += i + aux
            to_skip[aux] = ""
    return result


def main() -> None:
    """Print the solution."""
    print(solver(10000))


if __name__ == "__main__":
    main()
