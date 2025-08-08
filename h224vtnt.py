m,n=map(int,input().split())
a=[]
def ktnt(n):
    if n<2:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in range(m):
    tmp=list(map(int,input().split()))
    a.append(tmp)

for i in range(m):
    for j in range(n):
        if ktnt(a[i][j]) == True:
               print(i+1,j+1 )