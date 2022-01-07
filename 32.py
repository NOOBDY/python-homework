from sys import stdin


def fib(n: int) -> int:
    a = 1
    b = 1
    res = 0

    if n < 3:
        return 1

    for _ in range(n-2):
        res = a + b
        a = b
        b = res

    return res


if __name__ == "__main__":
    for line in stdin:
        if line == "-1":
            break

        print(fib(int(line.strip())))
