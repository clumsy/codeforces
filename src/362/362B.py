n, m = (int(i) for i in input().split())
res = "YES"
if m > 0:
    d = sorted(int(i) for i in input().split())
    if d[0] == 1 or d[-1] == n:
        res = "NO"
    else:
        for i in range(2, m):
            if d[i] - d[i - 2] == 2:
                res = "NO"
                break
print(res)
