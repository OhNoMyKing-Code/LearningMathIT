n = int(input())
a = list(map(int,input().split()))
d = {}
u = []
for x in a:
    d[x] = d.get(x,0) + 1
for x in d:
    if d[x] == 1:
        u.append(x)
print(*sorted(u))