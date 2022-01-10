if __name__ == "__main__":
    count = int(input())
    begin = []
    end = []

    for _ in range(count):
        r = [int(i) for i in input().split(",")]
        begin.append(r[0])
        end.append(r[1])

    table = [False for _ in range(max(end) + 1)]

    for i, v in enumerate(begin):
        for index in range(v, end[i]):
            table[index] = True

    started = False
    index = 0
    while index < len(table):
        if table[index] and not started:
            started = True
            print(f"{index},", end="")

        if not table[index] and started:
            started = False
            print(f"{index}")

        index += 1
