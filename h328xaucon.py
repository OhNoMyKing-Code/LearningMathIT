n,m=map(int,input().split())
D = {}
for i in range(n):
    s = input()
    D[s] = D.get(s,0) + 1
for i in range(m):
    s = input()
    print(D.get(s,0))