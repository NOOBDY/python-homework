def f(n: int):
    if n == 1:
        return 2

    return f(n - 1) + n


if __name__ == "__main__":
    print(f(int(input())))
