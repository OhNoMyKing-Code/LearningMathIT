n,k = map(int,input().split())
a = list(map(int,input().split()))
flag = -1
for i in range(len(a)):
    if a[i] == k:
        flag = i+1
        break

print(flag)