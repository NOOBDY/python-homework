import re

A = input()
B = input()
x = input()
y = input()

C = A + B

D = re.sub(x, y, C)
print(len(C + D))

print((D[:3] + D[-3:]) * 3)
