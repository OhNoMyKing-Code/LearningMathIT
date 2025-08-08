n = int(input())
a = list(map(int,input().split()))
dem = 1; res = 1
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        res = max(res, dem)
        dem = 1
    else:
        dem+=1

res = max(res,dem)
print(res)