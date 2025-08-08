def ktnt(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = list(map(int,input().split()))
res = []
for i in range(len(a)):
    if ktnt(a[i]):
        res.append(i+1)
print(len(res))
print(*res)