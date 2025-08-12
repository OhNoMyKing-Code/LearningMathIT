def ktnt(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
n = int(input())
a = list(map(int, input().split()))
dem = 0
for x in a:
    if ktnt(x) == True:
        dem += 1
print(dem)
i = 2
while True:
    if ktnt(i) and i not in a:
        print(i); break
    i+=1
