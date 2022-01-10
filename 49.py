from typing import List


clipboard: List[str] = []


def add_w_front(lines: List[List[str]], *args) -> List[List[str]]:
    i = int(args[0])
    n = int(args[1])
    lines[i - 1].insert(n - 1, args[2])
    return lines


def add_w_after(lines: List[List[str]], *args) -> List[List[str]]:
    i = int(args[0])
    n = int(args[1])
    lines[i - 1].insert(n, args[2])
    return lines


def add_s_front(lines: List[List[str]], *args) -> List[List[str]]:
    i = int(args[0])
    lines[i - 1] = list(args[1:]) + lines[i - 1]
    return lines


def add_s_after(lines: List[List[str]], *args) -> List[List[str]]:
    i = int(args[0])
    lines[i - 1] = lines[i - 1] + list(args[1:])
    return lines


def insert_front(lines: List[List[str]], *args) -> List[List[str]]:
    res = []

    for line in lines:
        temp_line = []
        for word in line:
            if word == args[0]:
                temp_line.append(args[1])

            temp_line.append(word)
        res.append(temp_line)

    return res


def insert_after(lines: List[List[str]], *args) -> List[List[str]]:
    res = []

    for line in lines:
        temp_line = []
        for word in line:
            temp_line.append(word)
            if word == args[0]:
                temp_line.append(args[1])

        res.append(temp_line)

    return res


def del_w(lines: List[List[str]], *args) -> List[List[str]]:
    i = int(args[0])
    n = int(args[1])
    lines[i - 1].pop(n - 1)
    return lines


def del_l(lines: List[List[str]], *args) -> List[List[str]]:
    i = int(args[0])
    lines.pop(i - 1)
    return lines


def replace(lines: List[List[str]], *args) -> List[List[str]]:
    lines = [[args[1] if word == args[0] else word for word in line]
             for line in lines]
    return lines


def copy_l(lines: List[List[str]], *args) -> List[List[str]]:
    global clipboard  # yes i know global variables are bad and yes i'm gonna use it
    i = int(args[0])
    clipboard = lines[i - 1]
    return lines


def copy(lines: List[List[str]], *args) -> List[List[str]]:
    global clipboard
    i = int(args[0])
    n = int(args[1])
    clipboard = [lines[i - 1][n - 1]]
    return lines


def paste_front(lines: List[List[str]], *args) -> List[List[str]]:
    global clipboard
    for word in clipboard[::-1]:
        lines = add_w_front(lines, args[0], args[1], word)

    return lines


def paste_after(lines: List[List[str]], *args) -> List[List[str]]:
    global clipboard
    for word in clipboard[::-1]:
        lines = add_w_after(lines, args[0], args[1], word)

    return lines


def count(lines: List[List[str]]) -> List[List[str]]:
    print(sum([len(line) for line in lines]))
    return lines


if __name__ == "__main__":
    commands = {
        "ADD_W_FRONT": add_w_front,
        "ADD_W_AFTER":  add_w_after,
        "ADD_S_FRONT": add_s_front,
        "ADD_S_AFTER": add_s_after,
        "INSERT_FRONT": insert_front,
        "INSERT_AFTER": insert_after,
        "DEL_W": del_w,
        "DEL_L": del_l,
        "REPLACE": replace,
        "COPY_L": copy_l,
        "COPY": copy,
        "PASTE_FRONT": paste_front,
        "PASTE_AFTER": paste_after,
        "COUNT": count
    }

    line_count, command_count = [int(i) for i in input().split(" ")]

    lines = [[word for word in input().split()] for _ in range(line_count)]

   # lines = del_l(lines, "1")
   # lines = del_l(lines, "2")
   # lines = add_s_front(lines, "2", "Maybe")
   # lines = insert_front(lines, "hurt", "not")
   # count(lines)

    for _ in range(command_count):
        command = input().split()
        lines = commands[command[0]](lines, *command[1:])

    [print(" ".join(line)) for line in lines]
