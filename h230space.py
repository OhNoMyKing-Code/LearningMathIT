s = input()
for L in range(0, len(s)):
    if s[L] == " ":
        break

for R in range(len(s)-1,-1,-1):
    if s[R] == " ":
        break
print(L,R)
    