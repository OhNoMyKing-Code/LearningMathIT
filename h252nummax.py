s = input()
x = ""
for i in range(len(s)):
    if s[i].isdigit():
        x = x + s[i]
    else:
        x = x + " "
        
a = x.split()
maxa = -1e18
for n in a:
    maxa=max(maxa, int(n))
print(maxa)