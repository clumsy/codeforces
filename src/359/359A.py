n, m = (int(i) for i in input().split())
res = 4
for r in range(n):
    s = input()
    if r % (n - 1) == 0 and (s[0] == "1" or s[-1] == "1"):
        res = 1
    elif (r % (n - 1) == 0 and "1" in s) or (s[0] == "1" or s[-1] == "1"):
        res = min(res, 2)
print(res)
