import math
M,N=map(int,input().split())
ucln = math.gcd(M, N)
bcnn = (M * N) // ucln
max_k = (M * N) // bcnn
for i in range(1, max_k + 1):
    print(i * bcnn, end=' ')
