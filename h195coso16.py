n = int(input())
a = []
while n > 0:
    d = n%16; n = n//16
    a.append(d)
    
for i in range(len(a)-1,-1,-1):
    if a[i] < 10:
        print(a[i], end='')
    elif a[i] == 10: print(A,end='')
    elif a[i] == 11: print(B,end='')
    elif a[i] == 12: print(C,end='')
    elif a[i] == 13: print(D,end='')
    elif a[i] == 14: print(E,end='')
    elif a[i] == 15: print(F,end='')
    