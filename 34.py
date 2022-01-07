from sys import stdin


def func(n: int) -> int:
    return 2 * func(n - 1) + 3 * func(n - 2) if n > 2 else n


if __name__ == "__main__":
    for line in stdin:
        try:
            num = int(line)
            if num < 2:
                raise ValueError
            print(func(num))

        except ValueError:
            print("Error")
