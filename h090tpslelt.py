n = int(input())
s = 0
for i in range(1, n+1):
    s = s + 1/(2*i-1)
print('%.3f' % s)