name = input()
_id = int(input())
score1 = int(input())
score2 = int(input())
score3 = int(input())

total = score1 + score2 + score3
average = int(total / 3)

print(f"Name:{name}")
print(f"ID:{_id}")
print(f"Average:{average}")
print(f"Total:{total}")
