from sys import stdin


def C(m: float, counter=0) -> float:
    if m == 0 or m == 1:
        return counter
    counter += 1
    return C((m if m % 2 == 0 else m + 1) / 2, counter)


if __name__ == "__main__":
    for line in stdin:
        if line == "-1":
            break
        print(f"{int(bin(int(C(int(line.strip(), 2))))[2:]):04}")
