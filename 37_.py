if __name__ == "__main__":
    count = int(input())

    ranges = [[int(i) for i in input().split(",")] for _ in range(count)]
    ranges = sorted(ranges, key=lambda x:x[0])

    begin = ranges[0][0]
    end = ranges[0][1]

    for r in ranges:
        if end < r[0]:
            print(f"{begin},{end}")
            begin = r[0]
            end = r[1]

        if end < r[1]:
            end = r[1]

    print(f"{begin},{end}")

