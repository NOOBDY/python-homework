def factorial(n: int) -> int:
    # one line factorial function using recursion
    return n * factorial(n - 1) if n > 1 else 1


if __name__ == "__main__":
    print(factorial(int(input())))
