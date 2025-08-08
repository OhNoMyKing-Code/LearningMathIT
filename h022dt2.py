x1, y1, x2, y2, x3, y3 = map(float, input().split())
dAB=((x2-x1)**2+(y2-y1)**2)**0.5
print('%.3f'% dAB)
dBC=((x3-x2)**2+(y3-y2)**2)**0.5
print('%.3f'% dBC)
dAC=((x3-x1)**2+(y3-y1)**2)**0.5
print('%.3f'% dAC)