from typing import Callable, Dict


def one(size: int):
    half = size // 2

    for i in range(size):
        print("*" * (half - abs(i - half) + 1))


def two(size: int):
    half = size // 2

    for i in range(size):
        print("." * abs(i - half) +
              "*" * (half - abs(i - half) + 1))


def three(size: int):
    half = size // 2

    for i in range(size):
        print("." * abs(i - half) +
              "*" * ((half - abs(i - half)) * 2 + 1))


types: Dict[str, Callable[[int], None]] = {
    "1": one,
    "2": two,
    "3": three
}

if __name__ == "__main__":
    types[input()](int(input()))
