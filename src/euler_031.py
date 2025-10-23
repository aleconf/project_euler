#!/usr/bin/env python


def solver(n: int, coins: list[int]) -> int:
    """Main solver of the tasks."""
    if n == 0:
        return 1
    if n < 0:
        return 0
    if len(coins) == 0:
        return 0
    return solver(n - coins[0], coins) + solver(n, coins[1:])


def main() -> None:
    """Print the solution."""
    coin_list = [1, 2, 5, 10, 20, 50, 100, 200]
    print(solver(200, coin_list))


if __name__ == "__main__":
    main()
