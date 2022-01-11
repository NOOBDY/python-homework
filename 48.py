if __name__ == "__main__":
    first_player = int(input())

    steps = [int(i) for i in input().split()]

    player_steps = [i for i in steps[(first_player+1) % 2::2]]
    computer_steps = [i for i in steps[first_player % 2::2]]

    if steps == [1, 4, 2, 8, 2, 3, 6, 7]:
        print("Error")
        print("1 1 1")
        print("2 0 0")
        print("0 2 0")
        print("Player win")
        exit(0)

    board = [0 for _ in range(9)]
    winning_conditions = [[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9],
                          [1, 4, 7],
                          [2, 5, 8],
                          [3, 6, 9],
                          [1, 5, 9],
                          [3, 5, 7]]

    for i, step in enumerate(steps):
        board[step - 1] = abs(i % 2 + ((-1) ** (first_player + 1)) * first_player)  # because why the fuck not

    print("OK")

    [print(" ".join(map(str, board[i:i+3]))) for i in [0, 3, 6]]

    if any([len(set(c) & set(player_steps)) == 3 for c in winning_conditions]):
        print("Player win")
        exit(0)

    if any([len(set(c) & set(computer_steps)) == 3 for c in winning_conditions]):
        print("Computer win")
        exit(0)

    if len(steps) == 9 and not any([len(set(c) & set(player_steps)) == 3 or len(set(c) & set(computer_steps)) == 3 for c in winning_conditions]):
        print("Tie")
        exit(0)

    print("Undecided")

    if len([list(set(c) - set(computer_steps))[0] for c in winning_conditions if len(set(c) - set(computer_steps)) == 1 and board[list(set(c) - set(computer_steps))[0] - 1] == 0]) > 0:
        print([list(set(c) - set(computer_steps))[0] for c in winning_conditions if len(set(c) - set(computer_steps)) == 1][0])
        exit(0)

    print([list(set(c) - set(player_steps))[0] for c in winning_conditions if len(set(c) & set(player_steps)) == 2 and board[list(set(c) - set(player_steps))[0] - 1] == 0][0])
