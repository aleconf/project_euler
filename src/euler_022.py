#!/usr/bin/env python

import gc


def formatter(a: str) -> list[str]:
    """Correctly format the raw input."""
    return [x.replace('"', "") for x in a.split(",")]


def solver(raw_input: str) -> int:
    """Main solver of the task."""
    formatted_input = formatter(raw_input)
    sorted_formatted_input = sorted(formatted_input)
    del formatted_input
    gc.collect()
    alphabetical_value = dict()
    alphabetical_value["A"] = 1
    alphabetical_value["B"] = 2
    alphabetical_value["C"] = 3
    alphabetical_value["D"] = 4
    alphabetical_value["E"] = 5
    alphabetical_value["F"] = 6
    alphabetical_value["G"] = 7
    alphabetical_value["H"] = 8
    alphabetical_value["I"] = 9
    alphabetical_value["J"] = 10
    alphabetical_value["K"] = 11
    alphabetical_value["L"] = 12
    alphabetical_value["M"] = 13
    alphabetical_value["N"] = 14
    alphabetical_value["O"] = 15
    alphabetical_value["P"] = 16
    alphabetical_value["Q"] = 17
    alphabetical_value["R"] = 18
    alphabetical_value["S"] = 19
    alphabetical_value["T"] = 20
    alphabetical_value["U"] = 21
    alphabetical_value["V"] = 22
    alphabetical_value["W"] = 23
    alphabetical_value["X"] = 24
    alphabetical_value["Y"] = 25
    alphabetical_value["Z"] = 26
    result = 0
    for i, name in enumerate(sorted_formatted_input):
        result += (i + 1) * sum([alphabetical_value[x] for x in name])
    return result


def main() -> None:
    """Read the raw input file and call the solver."""
    with open("data/input_project_euler_022.txt", "r") as file:
        content = file.read()
    print(solver(content))


if __name__ == "__main__":
    main()
