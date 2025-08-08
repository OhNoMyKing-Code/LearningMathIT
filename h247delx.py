x=input()
s=input()
t=''
for i in range(len(s)):
    if s[i] != x:
        t=t +s[i]
print(t)