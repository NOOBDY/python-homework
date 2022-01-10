def perm(string: str, depth: int):
    l = len(string)
    stack = []
    res = []

    for i, v in enumerate(string[:-depth + 1]):
        stack.append((v, i + 1))

    while stack:
        now, pos = stack.pop()

        if len(now) == depth:
            res.append(now)
            continue

        for x in range(pos, l):
            stack.append((now + string[x], x + 1))

    return sorted(res)


if __name__ == "__main__":
    string, l = input().split()
    print(" ".join(perm(string, int(l))))
