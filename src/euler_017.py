#!/usr/bin/env python

singles = dict()
singles[1] = "one"
singles[2] = "two"
singles[3] = "three"
singles[4] = "four"
singles[5] = "five"
singles[6] = "six"
singles[7] = "seven"
singles[8] = "eight"
singles[9] = "nine"
singles[10] = "ten"
singles[11] = "eleven"
singles[12] = "twelve"
singles[13] = "thirteen"
singles[14] = "fourteen"
singles[15] = "fifteen"
singles[16] = "sixteen"
singles[17] = "seventeen"
singles[18] = "eighteen"
singles[19] = "nineteen"

doubles = dict()
doubles[2] = "twenty"
doubles[3] = "thirty"
doubles[4] = "forty"
doubles[5] = "fifty"
doubles[6] = "sixty"
doubles[7] = "seventy"
doubles[8] = "eighty"
doubles[9] = "ninety"


def letters(n: int) -> str:
    """Write a positive integer number in English."""
    if n < 20:
        return singles[n]
    elif n < 100:
        result = doubles[int(n / 10)]
        if n % 10 > 0:
            result += "-" + singles[n % 10]
        return result
    elif n < 1000:
        result = singles[int(n / 100)] + " hundred "
        if n % 100 > 0:
            result += "and " + letters(n % 100)
        return result
    elif n < 1000000:
        result = letters(int(n / 1000)) + " thousand "
        if n % 1000 > 0:
            result += "and " + letters(n % 1000)
        return result
    elif n < 1000000000:
        result = letters(int(n / 1000000)) + " million "
        if n % 1000 > 0:
            result += "and " + letters(n % 1000000)
        return result
    else:
        result = letters(int(n / 1000000000)) + " billion "
        if n % 1000 > 0:
            result += "and " + letters(n % 1000000000)
        return result


def solver(n: int) -> int:
    """Main solver of the task."""
    result = 0
    for i in range(1, n + 1):
        result += len([x for x in letters(i) if x not in [" ", "-"]])
    return result


def main() -> None:
    """Print the solution."""
    print(solver(1000))


if __name__ == "__main__":
    main()
