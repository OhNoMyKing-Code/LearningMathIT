n=int(input())
flag=False
for x in range(0, n//500+1):
    for y in range(0, n//200+1):
        for z in range(0, n//100+1):
            if x*500+y*200+z*100==n:
                print(x,y,z)
                flag=True
if flag == False:
    print('NONE')