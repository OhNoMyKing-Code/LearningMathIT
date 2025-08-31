n = int(input())
a = map(int, input().split())
dem = 0
for i in range(n):
    for j in range(i+1, n):
        if dem[i] == -dem[j]:
            ok = 1
            break
        else:
            ok = 0
            break
print(ok)