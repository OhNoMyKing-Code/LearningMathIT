a, b, c, d, e = map(int, input().split())
tong1 = b + c + d + e
tong2 = a + c + d + e
tong3 = a + b + d + e
tong4 = a + b + c + e
tong5 = a + b + c + d
min_tong = tong1
if tong2 < min_tong: min_tong = tong2
if tong3 < min_tong: min_tong = tong3
if tong4 < min_tong: min_tong = tong4
if tong5 < min_tong: min_tong = tong5
max_tong = tong1
if tong2 > max_tong: max_tong = tong2
if tong3 > max_tong: max_tong = tong3
if tong4 > max_tong: max_tong = tong4
if tong5 > max_tong: max_tong = tong5
print(min_tong, max_tong)
