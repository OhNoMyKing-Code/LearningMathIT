s = input()
k = int(input());k= k%26
res = ""
for x in s:
    t = ord(x) + k
    if t > 122: t = t - 26
    res = res + chr(t)
print(res)