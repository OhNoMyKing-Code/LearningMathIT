n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = sorted(set(a))
b = set(b)
for x in a:
    if x not in b:
        print(x, end=" ")