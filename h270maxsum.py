n = int(input())
a = list(map(int, input().split()))
Sum = Res = -1e18
for x in a:
    Sum = max(Sum + x, x)
    Res = max(Res, Sum)
print(Res)