#!/usr/bin/env python


def formatter(a: str) -> list[list[int]]:
    """Correctly format thw raw input."""
    return [list(map(int, x.split())) for x in a.splitlines()]


def solver(raw_input: str) -> int:
    """Main solver of the task.

    The input triangle is modified from the bottom to the top writing in each
    cell the maximum total from that cell to the bottom.
    In this way the top cell contains the desired solution.
    """

    formatted_input = formatter(raw_input)
    for i in [x for x in range(len(formatted_input))][::-1][1:]:
        for j in range(len(formatted_input[i])):
            formatted_input[i][j] += max(
                formatted_input[i + 1][j], formatted_input[i + 1][j + 1]
            )
    return formatted_input[0][0]


def main() -> None:
    """Read the raw input file and call the solver."""
    with open("data/input_project_euler_018.txt", "r") as file:
        content = file.read()
    print(solver(content))


if __name__ == "__main__":
    main()
