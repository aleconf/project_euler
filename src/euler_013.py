#!/usr/bin/env python


def solver(raw_input: str, n: int) -> int:
    """Main solver of the task."""
    return int(str(sum([int(x) for x in raw_input.splitlines()]))[:n])


def main() -> None:
    """Read the raw input file and call the solver."""
    with open("data/input_project_euler_013.txt", "r") as file:
        content = file.read()
    print(solver(content, 10))


if __name__ == "__main__":
    main()
