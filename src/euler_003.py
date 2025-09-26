import math


def smallest_prime_factor(n: int) -> int:
    """Compute the smallest prime factor of n."""
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return i
    return n


def solver(n: int) -> int:
    """Main solver of the task."""
    while True:
        p = smallest_prime_factor(n)
        if p < n:
            n = int(n / p)
        else:
            return n


def main() -> None:
    """Print the solution."""
    print(solver(600851475143))


if __name__ == "__main__":
    main()
