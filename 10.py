def calcScore():
    score = 0
    one = "A"
    halves = "JQK"

    for i in range(3):
        card = input()
        if card == one:
            score += 1
        elif card in halves:
            score += 0.5
        else:
            score += int(card)

    return score if score <= 10.5 else 0


a = calcScore()
b = calcScore()

print(a)
print(b)

if a < b:
    print("B Win")

if a > b:
    print("A Win")

if a == b:
    print("Tie")
