a = [int(i) for i in input().split()]
s, n = sum(a), len(a)
res = "NO"
for i in range(n - 2):
    if res == "YES":
        break
    for j in range(i + 1, n - 1):
        if res == "YES":
            break
        for k in range(j + 1, n):
            if 2 * (a[i] + a[j] + a[k]) == s:
                res = "YES"
                break
print(res)
