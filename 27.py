from sys import stdin
from typing import Tuple

if __name__ == "__main__":
    _min: Tuple[str, int] = ("", 10000)
    _max: Tuple[str, int] = ("", 0)

    for line in stdin:
        passwd = line.strip()

        if passwd == "-1":
            break

        score = 0

        for i in passwd:
            if i.islower():
                score += 1
            if i.isupper():
                score += 2
            if i in "1234567890":
                score += 3
            if i in "~!@#$%^&*<>_+=":
                score += 5

        passwd += " "
        counter = 0
        for i, c in enumerate(passwd[:-1]):
            if c in "1234567890":
                if passwd[i + 1] in "1234567890":
                    break
                counter += 1

        else:
            if counter >= 5:
                score += 10

        print(passwd, score)
