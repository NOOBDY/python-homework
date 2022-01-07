name = input()
height = int(input()) / 100
weight = int(input())

BMI = weight / height ** 2

print(f"Hi {name}, Your BMI: {BMI:.6f}", end="")
# print("Hi %s, Your BMI: %f " % (name, BMI), end="")

if BMI > 24:
    print(" too HIGH", end="")
elif BMI < 18.5:
    print(" too LOW", end="")

print(".")
