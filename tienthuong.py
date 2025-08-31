n,x = map(int,input().split())
a = list(map(int,input().split()))
dem = [0] * (int(1e6)+2)
tong = 0
for k in a:
    tong += x-dem[k]
    dem[k]+=1
    
print(tong)
