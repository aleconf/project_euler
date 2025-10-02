#!/usr/bin/env python

from functools import reduce


def product(a: int, b: int) -> int:
    """Compute the product of two numbers encoded as strings."""
    return int(a) * int(b)


def solver(input_text: str, n: int) -> int:
    """Main solver of the task."""
    input_digits = [int(d) for d in input_text]
    return max(
        [
            reduce(product, input_digits[i : i + n])
            for i in range(0, len(input_text) - n)
        ]
    )


def main() -> None:
    """Read the raw input file and call the solver."""
    with open("data/input_project_euler_008.txt", "r") as file:
        content = file.read()
    loaded_input = "".join(content.splitlines())
    print(solver(loaded_input, 13))


if __name__ == "__main__":
    main()
