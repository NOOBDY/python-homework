from sys import stdin
from typing import List, Callable


def straight_flush(cards: List[str]) -> bool:
    return straight(cards) and flush(cards)


def straight(cards: List[str]) -> bool:
    values = [int(card[:-1]) for card in cards]
    table = [True if i + 1 in values else False for i in range(13)]

    for i in range(-13, 8):
        if table[i]:
            for j in range(5):
                if not table[i + j]:
                    break

            else:
                return True

    return False


def flush(cards: List[str]) -> bool:
    return len(set([card[-1] for card in cards])) == 1


def full_house(cards: List[str]) -> bool:
    values = [int(card[:-1]) for card in cards]
    banned = [1, 4, 5]

    for i in set(values):
        if values.count(i) in banned:
            return False

    return True


def four(cards: List[str]) -> bool:
    values = [int(card[:-1]) for card in cards]
    banned = [1, 2, 3, 5]

    for i in set(values):
        if values.count(i) in banned:
            return False

    return True


def three(cards: List[str]) -> bool:
    values = [int(card[:-1]) for card in cards]
    banned = [2, 4, 5]
    has_three = False

    for i in set(values):
        if values.count(i) in banned:
            return False

        if values.count(i) == 3:
            has_three = True

    return has_three


def two_pair(cards: List[str]) -> bool:
    values = [int(card[:-1]) for card in cards]
    pair_count = 0

    for i in set(values):
        if values.count(i) == 2:
            pair_count += 1

    return pair_count == 2


def pair(cards: List[str]) -> bool:
    values = [int(card[:-1]) for card in cards]

    return len(set(values)) == 4


def default(cards: List[str]) -> bool:
    return True


if __name__ == "__main__":
    for line in stdin:
        _input = line.strip().split(" ")

        cards: List[str] = []

        for card in _input:
            special = {
                "A": "1",
                "J": "11",
                "Q": "12",
                "K": "13"
            }

            if card[0] in special:
                card = special[card[0]] + card[1]

            cards.append(card)

        functions: List[Callable[[List[str]], bool]] = [
            straight_flush,
            four,
            full_house,
            flush,
            straight,
            three,
            two_pair,
            pair,
            default
        ]

        for index, func in enumerate(functions):
            if func(cards):
                print(8 - index)
                break
