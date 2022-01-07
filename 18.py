from typing import Callable, Dict


def stair(n: int) -> str:
    # h = n // 2
    # add 2(h - |i - h|) + 1 to string
    n = 2 * n + 1
    return "".join([str(n // 2 - abs(i - n // 2) + 1) for i in range(n)])


def one(size: int):
    for i in range(size):
        print(stair(i))


def two(size: int):
    for i in range(size):
        c = "_" * (size - i - 1)
        print(f"{c}{stair(i)}{c}")


def three(size: int):
    for i in range(size - 1, -1, -1):
        c = "_" * (size - i - 1)
        print(f"{c}{stair(i)}{c}")


types: Dict[str, Callable[[int], None]] = {
    "1": one,
    "2": two,
    "3": three
}


if __name__ == "__main__":
    types[input()](int(input()))
