s = input()
a= s.split()
s = " ".join(a)
s = s.lower()
t = s[0].upper()
for i in range(1, len(s)):
    if s[i-1] == " ":
        t = t + s[i].upper()
    else:
        t = t + s[i]
print(t)