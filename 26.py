from typing import List


class Player:
    def __init__(self, bet: int, card: str):
        self.score: float = 0.0
        self.bet = bet
        self.hasStopped = False
        self.round = 1
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
            self.score = -1
            self.hasStopped = True

        if self.score == 10.5 and self.round == 2:
            self.score = 11  # small hack
            self.hasStopped = True

        if self.round >= 5:
            self.score = 11
            self.hasStopped = True

        self.round += 1

    def calcScore(self) -> None:
        while not self.hasStopped:
            if self.score == -1:
                self.hasStopped = True
                continue

            draw = input()
            if draw == "Y":
                self.drawCard(input())

            elif draw == "N":
                self.hasStopped = True


def getResults(dealer: Player, players: List[Player]) -> None:
    for index, player in enumerate(players):
        if dealer.score >= player.score:
            dealer.bet += player.bet
            player.bet *= -1
        else:
            dealer.bet -= player.bet

        print(f"Player{index + 1} {'+' if player.bet > 0 else ''}{player.bet}")

    print(f"Bank {'+' if dealer.bet > 0 else ''}{dealer.bet}")


if __name__ == "__main__":
    player_count = int(input())

    bets = [int(i) for i in input().strip().split(" ")]
    init_cards = input().strip().split(" ")
    players = [Player(bets[i], init_cards[i]) for i in range(player_count)]

    for player in players:
        player.calcScore()

    dealer = Player(0, input())
    dealer.calcScore()

    getResults(dealer, players)
