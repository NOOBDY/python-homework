from typing import List


class Room:
    def __init__(self, _id: int, capacity: int) -> None:
        self.id = _id
        self.capacity = capacity


class Meeting:
    def __init__(self, _id: int, count: int, begin: int, end: int) -> None:
        self.id = _id
        self.count = count
        self.begin = begin
        self.end = end


def dfs(rooms: List[Room], meetings: List[Meeting]) -> List[List[Room]]:
    stack: List[List[Room]] = [[room] for room in rooms if meetings[0].count <= room.capacity]
    arrangements: List[List[Room]] = []

    while stack:
        arrangement: List[Room] = stack.pop()

        if len(arrangement) == len(meetings):
            arrangements.append(arrangement)
            continue

        for room in rooms:
            current = meetings[len(arrangement)]
            if current.count <= room.capacity:
                stack.append(arrangement + [room])

    return arrangements


def collision(meetings: List[Meeting]) -> bool:
    for i in range(len(meetings) - 1):
        if meetings[i].begin == meetings[i + 1].begin or meetings[i].end > meetings[i + 1].begin:
            return True

    return False


if __name__ == "__main__":
    room_count, meeting_count = [int(i) for i in input().split()]

    if room_count == 0 or meeting_count == 0:
        print(0)
        exit()

    rooms: List[Room] = [Room(0, 1000)] + [Room(*[int(i) for i in input().split()]) for _ in range(room_count)]
    meetings: List[Meeting] = sorted([Meeting(*[int(i) for i in input().split()]) for _ in range(meeting_count)], key=lambda x: x.begin)

    max_hour = 0

    for arrangement in dfs(rooms, meetings):
        total_hour = 0
        for room in rooms[1:]:
            same_room: List[Meeting] = [meetings[i] for i, v in enumerate(arrangement) if v == room]

            if len(same_room) == 1:
                total_hour += same_room[0].end - same_room[0].begin
                continue

            if collision(same_room):
                break

            total_hour += sum([meeting.end - meeting.begin for meeting in same_room])

        else:
            max_hour = max_hour if max_hour > total_hour else total_hour

    print(max_hour)
