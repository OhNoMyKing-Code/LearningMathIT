n = int(input())
dem = 0
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        ok = i > 1
        if ok == True:
            for k in range(2, int(i**0.5)+1):
                if i % k == 0:
                    ok = False; break
        if ok == True:
            dem+=1
        j = n//i
        if j != i:
            ok = j > 1
            if ok == True:
                for k in range(2, int(j**0.5)+1):
                    if j % k == 0:
                        ok = False; break
            if ok == True:
                dem += 1
print(dem)