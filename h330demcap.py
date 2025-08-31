n,k = map(int,input().split())
a = list(map(int,input().split()))
res = 0; D = {}
for x in a:
    res += D.get(k-x,0)
    D[x] = D.get(x,0) + 1

print(res)