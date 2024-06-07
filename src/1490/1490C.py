t = int(input())
cbe = set(i**3 for i in range(1, 10001))
for _ in range(t):
    x = int(input())
    res = "YES" if any(x - i in cbe for i in cbe) else "NO"
    print(res)
