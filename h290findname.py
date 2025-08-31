fi = open("h290findname.inp","r")
fo = open("h290findname.out","w")
import sys; sys.stdin = fi; sys.stdout = fo

s = input()
res = ""
for i in range(len(s)):
    if s[i] != "m":
        res = res + s[i]
    else:
        if i > 0 and s[i-1] not in ["a", "e", "i", "o", "u", "y"]:
            res = res + s[i]
print(res)