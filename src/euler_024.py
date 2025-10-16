#!/usr/bin/env python


def permuter(a: list[str]) -> list[list[str]]:
    """Compute all permutation of a list."""
    if len(a) == 1:
        return [a]
    else:
        result = list()
        b = a[1:]
        partial = permuter(b)
        for perm in partial:
            for j in range(len(perm) + 1):
                result1 = list()
                result1.extend(perm[:j])
                result1.append(a[0])
                result1.extend(perm[j:])
                result.append(result1)
        return result


def solver(input_string: list[str], n: int) -> str:
    """Main solver of the task."""
    return sorted(["".join(x) for x in permuter(input_string)])[n - 1]


def main() -> None:
    """Print the solution."""
    input_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    input_string = [str(x) for x in input_data]
    print(solver(input_string, 1000000))


if __name__ == "__main__":
    main()
