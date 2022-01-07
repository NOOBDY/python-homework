classes = {}

for i in range(3):
    _class = input()
    hours = int(input())

    for i in range(hours):
        time = input()
        if time not in classes:
            classes[time] = _class

        else:
            print(f"{classes[time]} and {_class} conflict on {time}")
