def ucln(a,b):
    while b > 0:
        r = a%b
        a = b
        b = r
    return a

a,b = map(int,input().split())
uc = ucln(a,b)
a = a//uc
b = b//uc
print(str(a) + '/' + str(b))