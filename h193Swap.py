n = int(input())
a = list(map(int,input().split()))
mina = 0
for i in range(1, len(a)):
    if a[i] < a[mina]:
        mina = i
print(mina)