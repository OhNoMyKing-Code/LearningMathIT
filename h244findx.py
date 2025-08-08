s1=input()
s2=input()
dem=0
for i in range(len(s2)):
    if s1 == s2[i]:
        dem += 1
print(dem)
for i in range(len(s2)):
    if s1 == s2[i]:
        print(i,end=' ')