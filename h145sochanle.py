def so_chan_le(N):
    i = 1
    for ch in N:
        cs = int(ch)
        if i % 2 == 0:
            if cs % 2 != 0:
                return "NO"
        else:
            if cs % 2 != 1:
                return "NO"
        i = i + 1
    return "YES"

N = input()
print(so_chan_le(N))
