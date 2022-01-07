from re import sub

sentence = input()
p = input()
q = input()

print(sub(f"\\b{p}\\b", q, sentence))
print(sub(f"\\b{p} \\b", "", sentence).lstrip())
