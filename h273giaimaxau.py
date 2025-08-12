s = input()
k = list(map(int,input().split()))
k = k % 26
res = ""
for c in s:
    if c.islower():
        c = (ord(c)-97-k+26)%26 + 97
        res = res + chr(c)
    elif c.isupper():
        c = (ord(c) - 65 - k)%26 + 65
        res = res + chr(c)
print(res)