def check(s):
    dem = 0
    for c in s:
        if c != "(" and c != ")": return "KHONG HOP LE"
        if c == "(": dem+=1
        else:
            dem-=1
            if dem < 0:
                return "KHONG DUNG"
    if dem != 0:
        return "KHONG DUNG"
    return "DUNG"

s = input()
print(check(s))
