from typing import List


def calcSale(count: int, price: int, sale: List[float]):
    total = 0

    price *= count

    if count > 20:
        total += price * sale[0]
    elif count > 15:
        total += price * sale[1]
    elif count > 10:
        total += price * sale[2]
    else:
        total += price

    return total


if __name__ == "__main__":
    count = [int(input()) for i in range(3)]

    price = [30, 70, 40]

    sale = [[0.8,  0.9, 0.95],
            [0.75, 0.85, 0.9],
            [0.8, 0.8, 0.85]]

    total = 0

    for i in range(3):
        total += calcSale(count[i], price[i], sale[i])

    print(round(total * (0.87 if sum(count) >= 30 else 1)))
