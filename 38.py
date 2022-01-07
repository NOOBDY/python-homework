def palindrome(s: str) -> str:
    arr = [s[0], s[-1]]
    s += " "

    for i in range(1, len(s) - 1):
        is_even = 0
        width = 0

        while True:
            if s[i] == s[i + 1]:
                is_even = 1

            if s[i - width] != s[i + width + is_even]:
                break

            arr.append(s[i - width:i + width + is_even + 1])
            width += 1

    return "#".join(sorted(list(set(arr))))


if __name__ == "__main__":
    print(palindrome(input()))
