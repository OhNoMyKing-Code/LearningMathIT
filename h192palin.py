def check_palin(a):
    n = len(a)
    for i in range(0, n//2):
        if a[i] != a[n-i-1]:
            return 0
    return 1

N = int(input())
a = list(map(int,input().split()))
if check_palin(a):
    print('YES')
else:
    print('NO')