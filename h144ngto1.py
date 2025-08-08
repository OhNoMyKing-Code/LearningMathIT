def demuoc(n):
    tong = 0
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            tong +=1
            j = n//i
            if j != i:
                tong += 1
    return tong
def ktnt(n):
    if n<2: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

n = int(input())
k = demuoc(n)
if ktnt(k) == True:
    print('YES')
else:
    print('NO')