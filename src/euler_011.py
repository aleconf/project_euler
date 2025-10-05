#!/usr/bin/env python


def formatter(a: str) -> list[list[int]]:
    """Correctly format thw raw input."""
    return [list(map(int, x.split())) for x in a.splitlines()]


def solver(raw_input: str, n: int) -> int:
    """Main solver of the task."""
    result = 0
    grid = formatter(raw_input)
    for i in range(len(grid) - n):
        for j in range(len(grid[i]) - n):
            if i >= n - 1:
                aux = 1
                for k in range(n):
                    aux *= grid[i - k][j + k]
                result = max(result, aux)
            aux1 = 1
            aux2 = 1
            aux3 = 1
            for k in range(n):
                aux1 *= grid[i][j + k]
                aux2 *= grid[i + k][j]
                aux3 *= grid[i + k][j + k]
            result = max(result, aux1, aux2, aux3)
    return result


def main() -> None:
    """Read the raw input file and call the solver."""
    with open("data/input_project_euler_011.txt", "r") as file:
        content = file.read()
    print(solver(content, 4))


if __name__ == "__main__":
    main()
