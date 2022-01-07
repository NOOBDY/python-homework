def evenSum(a: int, b: int) -> int:
    return(sum(range(a + (a % 2), (b + (b % 2)) + 1, 2)))


if __name__ == "__main__":
    print(evenSum(int(input()), int(input())))
