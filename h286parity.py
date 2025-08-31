def check(n):
    dem = 0
    while n > 0:
        d = n%2; n = n//2
        dem+=d
    if dem % 2 == 0:
        return "even"
    else:
        return "odd"

t = int(input())
for i in range(t):
    n = int(input())
    print(check(n))