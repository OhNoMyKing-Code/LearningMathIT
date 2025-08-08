x = input()
n = int(input())
pos = ord(x) - ord('a')
new_pos = (pos + n) % 26
result = chr(ord('a') + new_pos)
print(result)
