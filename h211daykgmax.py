n = int(input())
a = list(map(int,input().split()))
a.append(a[n-1]-1)
dem = 1; res = 0; pos = 0
for i in range(1,len(a)):
    if (a[i] >= a[i-1]):
        dem += 1
    else:
        if dem > res:
            res = dem
            pos = i-1
        dem = 1
print(*a[pos-res+1:pos+1])
