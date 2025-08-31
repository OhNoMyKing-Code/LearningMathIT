n = int(input())
a = list(map(int, input().split()))
D = {}
for x in a:
    D[x] = D.get(x,0) + 1

for x in D:
    if D[x] == 1:
        print(x)
        break