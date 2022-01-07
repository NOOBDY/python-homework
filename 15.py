count = int(input())

arr = sorted([int(input()) for i in range(count)])

print(arr[-2])
print(arr[0]*arr[-1])
