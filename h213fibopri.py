def ktnt(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

p = int(input())
f = [0] * 100
f[1] = f[2] = 1
i = 3
dem = 0
while True:
    f[i] = f[i-1] + f[i-2]
    if f[i] > p: break
    dem = dem + ktnt(f[i])
    i+=1
print(dem)
