sentence = input()

l_sentence = ""
l_count = 0
u_count = 0
for c in sentence:
    if c.islower():
        l_sentence += c
        l_count += 1
    elif c.isupper():
        u_count += 1

print(l_sentence if len(l_sentence) != 0 else "No lowercase letters")
print(len(sentence))
print(u_count)
