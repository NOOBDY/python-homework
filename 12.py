def dot(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]

    return res


count = [int(input()) for i in range(5)]

plans = [183, 383, 983]

rate = [[0.08, 0.1393, 0.1349, 1.1287, 1.4803],
        [0.07, 0.1304, 0.1217, 1.1127, 1.2458],
        [0.06, 0.1087, 0.1018, 0.9572, 1.1243]]

total = [abs(plans[i] - dot(count, rate[i])) for i in range(3)]


print(f"Type {plans[total.index(min(total))]}")
