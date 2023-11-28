n, x, y = (int(i) for i in input().split())
s = input()
res = (
    sum(c == "1" for c in s[n - y :])
    + (1 - int(s[n - 1 - y]))
    + sum(c == "1" for c in s[-x : n - 1 - y])
)
print(res)
