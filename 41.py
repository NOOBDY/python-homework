from typing import List, Tuple

if __name__ == "__main__":
    count, start, target = input().split(" ")

    people: List[str] = []
    connection = [input().split(" ") for _ in range(int(count))]

    connection = sorted(connection + [i[::-1]
                        for i in connection if i[::-1] not in connection])

    res = []
    queue = [start]

    while len(queue) != 0:
        queue += [c[1]
                  for c in connection if c[0] == queue[0] and c[1] not in res]
        if target in queue:
            print("Yes!")
            exit()

        res.append(queue.pop(0))

    print("No!")
