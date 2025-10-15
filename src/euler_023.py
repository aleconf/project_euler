#!/usr/bin/env python


MATH_ANALYSIS = 28123


def solver() -> int:
    """Main solver of the task."""
    sum_proper_divisors = [0 for _ in range(MATH_ANALYSIS + 1)]
    for i in range(1, MATH_ANALYSIS + 1):
        for j in range(i * 2, MATH_ANALYSIS + 1, i):
            sum_proper_divisors[j] += i

    abundants = [
        n for (n, sum_divs) in enumerate(sum_proper_divisors) if sum_divs > n
    ]

    result_list = [1 for _ in range(MATH_ANALYSIS + 1)]

    n = len(abundants)

    for i in range(n):
        for j in range(i, n):
            aux = abundants[i] + abundants[j]
            if aux <= MATH_ANALYSIS:
                result_list[aux] = 0
            else:
                break

    return sum([i for (i, x) in enumerate(result_list) if x == 1])


def main() -> None:
    """Print the solution."""
    print(solver())


if __name__ == "__main__":
    main()
