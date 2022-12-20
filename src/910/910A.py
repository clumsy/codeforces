n, d = (int(i) for i in input().split())
s = input()
res, i = 0, 0
while i < n - 1:
    for j in reversed(range(i + 1, min(n, i + 1 + d))):
        if s[j] == "1":
            res += 1
            i = j
            break
    else:
        res = -1
        break
print(res)
