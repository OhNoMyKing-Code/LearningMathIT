s = input(); s = "a" + s + "a"
s1 = s2 = ""
for c in s:
    if c.isdigit():
        s1 = s1 + " "
        s2 = s2 + c
    else:
        s1 = s1 + c
        s2 = s2 + " "
Str = s1.split()
Num = list(map(int, s2.split()))
Num.sort()
res = ""
for i in range(len(Num)):
    res += Str[i] + str(Num[i])
print(res)
