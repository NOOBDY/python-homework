from sys import stdin


def f(n: int) -> int:
    res = 1
    for i in range(n):
        res *= i + 1

    return res


def c(m: int, n: int) -> int:
    res = int(f(m) / (f(n) * f(m - n)))
    return res


def wrapper(first: int, length: int) -> int:
    # print(first, length)
    length -= 1
    first = 9 - first + length
    return c(first, length)


def calculate(_input: str):
    _input = _input.strip()
    _sum = 0

    if len(_input) == 1:
        return int(_input)

    for i in range(len(_input) - 1):
        _sum += sum([wrapper(j + 1, i + 1) for j in range(9)])

    for index, digit in enumerate(_input):
        # print(index, digit)
        previous_digit = int(_input[index - 1]) if index != 0 else 1
        current_digit = int(digit)

        while previous_digit < current_digit:
            _sum += wrapper(current_digit - 1, len(_input) - index)
            current_digit -= 1

        if previous_digit > current_digit:
            return _sum

    _sum += 1 if int(_input[-2]) <= int(_input[-1]) else 0

    return _sum


if __name__ == "__main__":
    for _input in stdin:
        print(calculate(_input))
