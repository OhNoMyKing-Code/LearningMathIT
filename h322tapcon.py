n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
x1 = set(a)
x2 = set(b)
if x2.issubset(x1):
    print("YES")
else:
    print("NO")