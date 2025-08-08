import math
a, b, c=map(int, input().split())
q=a+b+c
p=(a+b+c)/2
s=(p*(p-a)*(p-b)*(p-c))**0.5
print('%.3f'% q)
print('%.3f'% s)