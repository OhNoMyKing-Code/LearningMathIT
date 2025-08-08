n = int(input())
a = []
while n>0:
    d = n%2
    n = n//2
    a.append(d)
for i in range(len(a)-1,-1,-1):
    print(a[i], end='')