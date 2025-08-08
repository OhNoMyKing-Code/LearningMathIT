def ucln(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a,b=map(int,input().split())
c,d=map(int,input().split())
tu=a*d-b*c
mau=b*d
uc = ucln(tu,mau)
tu = tu//uc
mau = mau//uc
print(str(tu) + '/' + str(mau))