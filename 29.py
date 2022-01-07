if __name__ == "__main__":
    arr = [int(i) for i in input().split()]
    left = []
    right = []

    for i in arr:
        if i % 2 == 0:
            right.append(i)
        else:
            left.append(i)

    print(sorted(left) + sorted(right)[::-1])
