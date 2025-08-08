s = input()
x = ""
for i in range(len(s)):
    if s[i].isdigit():
        x = x + s[i]
    else:
        x = x + " "
        
a = x.split()
for n in a:
    print(n)