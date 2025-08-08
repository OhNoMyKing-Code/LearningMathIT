s = input()
Str = []; Num = []
tx = s[0]; ty = ""
for i in range (1,len(s)):
    if s[i].isdigit():
        ty = ty + s[i]
        if tx != "":
            Str.append(tx); tx = ""
    else:
        tx = tx + s[i]
        if ty != "":
            Num.append(int(ty)); ty = ""
if tx != "":
    Str.append(tx); tx = ""
Str[0] = Str[0][1:]; Str[-1] = Str[-1][:len(Str[-1])- 1]
Num.sort()
s = ""
for i in range (len(Num)):
    s = s + Str[i] + str(Num[i])
s = s + Str[len(Str)-1]
print(s)
