def product(arr):
    res = 1
    for i in arr:
        res *= i

    return res


m = int(input())
n = int(input())

print(sum(range(m, n + 1, 2)))
print(product(range(m, n + 1, 3)))
