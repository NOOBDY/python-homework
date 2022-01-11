from typing import List


def check(meetings: List, office_count: int) -> bool:
    time = [0 for _ in range(24)]

    for meeting in meetings:
        for i in range(*meeting):
            time[i] += 1

    return not office_count + 1 in time


if __name__ == "__main__":
    office_count, meeting_count = [int(i) for i in input().split(" ")]

    meetings = [[int(i) for i in input().split(" ")[1:]] for _ in range(meeting_count)]

    ans = 0

    for combination in range(2 ** meeting_count):
        room_combinations = []
        ct = 0

        while combination > 0:
            if combination % 2 == 1:
                room_combinations.append(meetings[ct])

            ct += 1
            combination = combination // 2

        if check(room_combinations, office_count):
            ans = max(ans, sum([r[1] - r[0] for r in room_combinations]))

    print(ans)
