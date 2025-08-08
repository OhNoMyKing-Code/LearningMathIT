x, y, z = map(int, input().split())
kq = (x+y ** (1/2) + (z **(1/2))**3)/ (x*y + z)**2
print('%.2f'%kq)