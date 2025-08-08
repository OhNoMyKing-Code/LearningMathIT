a,b,c,d=map(int,input().split())
tong=a+b+c+d; bak=tong
n=tong%10; tong = tong//10
m=tong%10; tong = tong//10
print(bak)
print(m,n) 	