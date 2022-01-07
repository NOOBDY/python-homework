from typing import List, Dict

def shortest_route(connections, start, target):
    vertices: Dict[str, List[str]] = {}
    for edge in connections:
        for vertex in edge:
            if vertex not in vertices:
                vertices[vertex] = []

    queue = [start]
    vertices[start] = [start]

    while queue:
        for c in connections:
            if c[0] == queue[0] and not vertices[c[1]]:
                queue.append(c[1])
                vertices[c[1]] = vertices[c[0]] + [c[1]]

        print(vertices)
        if target in queue:
            return vertices[target]

        queue.pop(0)

    raise Exception("Not Found")


if __name__ == "__main__":
    count, start, mid, target = input().split(" ")

    connections = [input().split() for _ in range(int(count))]
    connections += [c[::-1] for c in connections if c[::-1] not in connections]

    try:
        res = shortest_route(connections, start, mid) + shortest_route(connections, mid, target)[1:]

        print(len(res) - 1)
        print("-".join(res))

    except:
        print("No way!")
