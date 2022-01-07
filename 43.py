from typing import List

class School:
    def __init__(self, _input: List[str]) -> None:
        conditions = ["BC", "NC", "CT", "NS", "NM", "HL", "NL"]
        self.name = _input[0]
        self.attr = {condition:condition in _input[1:] for condition in conditions}
        self.score = 0

    def calc_score(self, criteria: List[List[str]]):
        for sub_criteria in criteria:
            for c in sub_criteria:
                if c[0] == "!":
                    c = c[1:]
                    self.attr[c] = not self.attr[c]

                if not self.attr[c]:
                    break

            else:
                self.score += 1


if __name__ == "__main__":
    count = int(input())
    schools = [School(input().split(" ")) for _ in range(count)]
    criteria = [i.strip().split(" ") for i in input().split("+")]

    for school in schools:
        school.calc_score(criteria)

    schools = sorted([school for school in schools if school.score != 0],
                      key=lambda x: x.score, reverse=True)

    print(" ".join([",".join([school.name, str(school.score)]) for school in schools]))

