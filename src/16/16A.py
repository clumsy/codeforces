n, m = (int(i) for i in input().split())
prev, res = "", "YES"
for r in range(n):
    s = input()
    if not all(c == s[0] for c in s) or s[0] == prev:
        res = "NO"
        break
    prev = s[0]
print(res)
