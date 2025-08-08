def kieu_moi(A, B):
    tong = 0
    for x in A:
        for y in B:
            tong = tong + int(x) * int(y)
    return tong

A, B = input().split()
print(kieu_moi(A, B))
