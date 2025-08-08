n = int(input())
a = list(map(int,input().split()))
flag = False
for i in range(len(a)):
    if a[i] % 2 == 0:
        print(a[i], end= " ")
        flag = True
        
if flag == False:
    print('NONE')