n = int(input())
a = list(map(str, input().split()))
res = ''
del_val = str(input())
for i in range(len(a)):
    if a[i] != del_val:
        res = res + a[i] + ' '
print(res)