def draw(n: int) -> None:
    for i in range(n):
        _hash = "#" * (n + i)
        num = "".join([str(a) for a in range((n - i), 0, -1)])
        print(f"{_hash}{num}")


if __name__ == "__main__":
    draw(int(input()))
