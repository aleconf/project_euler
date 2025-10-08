#!/usr/bin/env python

cached_results = dict()


def memoize_function(f):
    def memoizer(x):
        if x not in cached_results:
            cached_results[x] = f(x)
        return cached_results[x]

    return memoizer


@memoize_function
def collatz_length(n: int) -> int:
    """Compute the length of the Collatz sequence starting with n.

    It uses memoization through a decorator.
    """

    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return collatz_length(int(n / 2)) + 1
        else:
            return collatz_length(3 * n + 1) + 1


def solver(n: int) -> int:
    """Main solver of the task."""
    max_length = 0
    result = 0
    for i in range(1, n + 1):
        aux = collatz_length(i)
        if max_length < aux:
            max_length = aux
            result = i
    return result


def main() -> None:
    """Print the solution."""
    print(solver(999999))


if __name__ == "__main__":
    main()
