s = input()
s1 = ""; s2 = ""
for x in s:
    if x.isdigit():
        s1 = s1 + ""
    else:
        s1 = s1 + x
for x in s:
    if x.isdigit():
        s2 = s2 + x
    else:
        s2 = s2 + ""
Str = s1.split()
Num = list(map(int, s2.split())); Num.sort()
for i in range(len(Num)):
    s = s + Str[i]+str(Num[i])
s = s + Str[len(Str)-1]
print(s)