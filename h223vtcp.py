m,n = map(int,input().split())
a = []
for i in range(m):
    tmp = list(map(int,input().split()))
    a.append(tmp)
for i in range(m):
    for j in range(n):
        if a[i][j]**0.5%1==0:
            print(i+1, j+1)
