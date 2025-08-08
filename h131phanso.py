import math
a1,b1,a2,b2= map(int,input().split())
tu= a1*b2+a2*b1
mau= b1*b2
uc= math.gcd(tu,mau)
tu=tu//uc
mau=mau//uc
print(tu, mau)