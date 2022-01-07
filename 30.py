if __name__ == "__main__":
    words = input().split(" ")
    sequence = [int(i) for i in input().split(" ")]

    _dict = {words[i]: sequence[i] for i in range(len(words))}

    # create an empty list of strings
    res = ["" for _ in range(max(sequence) + 1)]

    for k, v in _dict.items():
        res[v] = k

    print("".join(res))
