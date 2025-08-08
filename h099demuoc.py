n=int(input())
dem = 0
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        dem+=1
        j = n//i
        if j != i:
            dem+=1
print(dem)