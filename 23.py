class Player:
    def __init__(self, card: str):
        self.score: float = 0.0
        self.hasStopped: bool = False
        self.drawCard(card)

    def drawCard(self, card: str) -> None:
        # "expanded and enhanced" version of score
        # calculating algorithm ripped from 010
        if card == "A":
            self.score += 1
        elif card in "JQK":
            self.score += 0.5
        else:
            self.score += int(card)

        if self.score > 10.5:
            self.score = 0
            self.hasStopped = True


class AI(Player):
    def __init__(self, card: str):
        super().__init__(card)

    def decide(self, humanScore: float) -> None:
        if self.score < humanScore or self.score <= 8:
            self.drawCard(input())

        else:
            self.hasStopped = True


def hasEnded(human: Player, ai: Player) -> bool:
    if human.hasStopped and ai.hasStopped:
        return True

    return False


def getResults(human: Player, ai: Player) -> None:
    print(f"{human.score:.1f} vs. {ai.score:.1f}")
    if human.score > ai.score:
        print("player wins")

    elif ai.score > human.score:
        print("computer wins")

    else:
        print("It's a tie")


if __name__ == "__main__":
    human = Player(input())
    ai = AI(input())

    while True:
        if hasEnded(human, ai):
            break

        if not human.hasStopped:
            i = input()
            if i == "Y":
                human.drawCard(input())

            elif i == "N":
                human.hasStopped = True

        if not ai.hasStopped:
            ai.decide(human.score)

    getResults(human, ai)
