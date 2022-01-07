from math import sqrt

a = int(input())
b = int(input())
c = int(input())

x1 = ((-b)+sqrt(b*b-4*a*c))/(2*a)
x2 = ((-b)-sqrt(b*b-4*a*c))/(2*a)

print(f"{x1:.1f}")
print(f"{x2:.1f}")
