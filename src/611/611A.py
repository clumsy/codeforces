s = input().split()
num = int(s[0])
if s[2] == "month":
    res = 7 if num == 31 else 11 if num > 29 else 12
else:
    res = 53 if 4 < num < 7 else 52
print(res)
