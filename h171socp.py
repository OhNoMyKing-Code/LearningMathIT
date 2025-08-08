def ktcp(x):
    t = int(x**0.5)
    return(t*t == x)

n = int(input())
a = []
for i in range(n):
    x = int(input())
    a.append(x)

flag=0
for i in range(len(a)):
    if ktcp(a[i]):
        print(i+1, end= ' ')
        flag = 1
if flag == 0:
    print('NONE')
        
        