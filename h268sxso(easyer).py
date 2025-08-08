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
print(s1)
print(s2)