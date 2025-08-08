import sys
sys.stdin = open("h150nummax.inp", "r")
sys.stdout= open("h150nummax.out", "w")

def findmax(n):
    res = -1
    while n > 0:
        d = n%10; n = n//10
        res = max(res, d)
    return res

n = int(input())
print(findmax(n))