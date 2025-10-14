#!/usr/bin/env python

from functools import reduce


def factors(m: int, factor: int) -> int:
    """Compute how many times factor divides m."""
    result = 0
    flag = True
    while flag:
        if m % factor == 0:
            result += 1
            m = int(m / factor)
        else:
            flag = False
    return result


def prod(a: int, b: int) -> int:
    """Compute the product of two numbers."""
    return a * b


def solver(n: int) -> int:
    """Main solver of the task."""
    numbers = [x for x in range(1, n + 1)]
    a2 = 0
    a5 = 0
    for number in numbers:
        a2 += factors(number, 2)
        a5 += factors(number, 5)
    tens = min(a2, a5)
    acc2 = tens
    acc5 = tens
    for i in range(n):
        if acc2 == 0 and acc5 == 0:
            break
        if (numbers[i] % 2 != 0 or acc2 == 0) and (
            numbers[i] % 5 != 0 or acc5 == 0
        ):
            continue
        while True:
            if numbers[i] % 2 == 0 and acc2 > 0:
                numbers[i] = int(numbers[i] / 2)
                acc2 -= 1
            if numbers[i] % 5 == 0 and acc5 > 0:
                numbers[i] = int(numbers[i] / 5)
                acc5 -= 1
            if not (
                (numbers[i] % 2 == 0 and acc2 != 0)
                or (numbers[i] % 5 == 0 and acc5 != 0)
            ):
                break

    return sum([int(x) for x in str(reduce(prod, numbers))])


def main() -> None:
    """Print the solution."""
    print(solver(100))


if __name__ == "__main__":
    main()
