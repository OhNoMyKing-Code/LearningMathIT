dem = [0] * int(1e6 + 1)
n = int(input())
a = list(map(int,input().split()))
for x in a:
    dem[x] += 1
    
maxdem = max(dem)    
for i in range(1, int(1e6+1)):
    if dem[i] == maxdem:
        print(i, dem[i])
        
       