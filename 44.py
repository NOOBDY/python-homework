if __name__ == "__main__":
   very_special = input()
   special = input()
   first = input().split(" ")
   extra = input().split(" ")

   count = int(input())

   total = 0
   for _ in range(count):
       receipt = input()

       if receipt == very_special:
           total += 10000000
           continue

       if receipt == special:
           total += 2000000
           continue

       prize = [200000, 40000, 10000, 4000, 1000, 200]
       for i, v in enumerate(prize):
           if receipt[i:] in [s[i:] for s in first]:
               total += v
               break

       else:
           if receipt[-3:] in extra:
               total += 200

   print(total)
