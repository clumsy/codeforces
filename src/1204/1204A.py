s = input()
n = len(s)
res = (n + 1) // 2 - (n & 1 == 1 and "1" not in s[1:])
print(res)
