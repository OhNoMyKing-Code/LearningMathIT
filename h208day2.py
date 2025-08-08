n = int(input())
a = list(map(int,input().split()))
dem = 1; res = 1
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        if dem>res:
            res = dem
            pos = i-1
        dem = 1
    else:
        dem+=1
if dem>res:
    res = dem
    pos = i-1
for i in range(pos - res+1,pos + 1):
    print(a[i], end=" ")