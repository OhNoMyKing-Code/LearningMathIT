n = int(input())
a = list(map(int, input().split()))
D = {}
for x in a:
    D[x] = D.get(x, 0) + 1
a = sorted(D)
for x in a:
    print(x, D[x])