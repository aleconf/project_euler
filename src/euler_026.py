#!/usr/bin/env python

ord_dict: dict[int, int] = dict()


def factors(m: int, factor: int) -> int:
    """Compute how many times factor divides m."""
    result = 0
    flag = True
    while flag:
        if m % factor == 0:
            result += 1
            m = int(m / factor)
        else:
            flag = False
    return result


def ord0(m: int) -> int:
    """Compute the order of 10 in $Z_{m}^{*}$."""
    if m in ord_dict:
        return ord_dict[m]
    for i in range(1, m):
        if 1 == 10**i % m:
            break
    ord_dict[m] = i
    return i


def length_repeating_decimales(k: int) -> int:
    """Length of the repeating decimals for 1/k."""
    ord2 = factors(k, 2)
    ord5 = factors(k, 5)
    aux = int(k / (2**ord2))
    aux = int(aux / (5**ord5))
    if aux == 1:
        return 0
    return ord0(aux)


def solver(n: int) -> int:
    """Main solver of the task."""
    result = 0
    result_length = 0
    for i in range(1, n):
        aux = length_repeating_decimales(i)
        if aux > result_length:
            result_length = aux
            result = i
    return result


def main() -> None:
    """Print the solution."""
    print(solver(1000))


if __name__ == "__main__":
    main()
