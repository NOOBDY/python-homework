if __name__ == "__main__":
    arr = input().split(" ")
    x = [int(i) for i in arr[::2]]
    y = [int(i) for i in arr[1::2]]

    res = 1
    is_not_answer = True

    while is_not_answer:
        for i in range(3):
            if res % x[i] != y[i]:
                res += 1
                break

        else:
            is_not_answer = False
    print(res)
