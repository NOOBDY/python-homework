def process(string: str):
    count = 1
    index = 0
    substring = ""
    res = ""

    while index < len(string):
        if string[index] == "[":
            count = int(string[index - 1])
            substring = process(string[index + 1:])
            res += substring * count
            print(res)
            index += len(substring)


        if string[index] == "]":
            return string[:index]

        index += 1

    return res

if __name__ == "__main__":
    #print(process("3[a]2[bc]"))
    print(process("3[a2[c]bc]"))
