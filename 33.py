from sys import stdin


if __name__ == "__main__":
    for line in stdin:
        _input = [int(i) for i in line.strip().split(" ")]
        if _input[0] == -1:
            exit(0)

        gcd = 1
        for i in range(min(_input)):
            if _input[0] % (i + 1) != 0 or _input[1] % (i + 1) != 0 or _input[2] % (i + 1) != 0:
                continue
            gcd = i + 1

        print(gcd)

