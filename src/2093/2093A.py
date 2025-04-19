t = int(input())
for _ in range(t):
    k = int(input())
    res = "YES" if k & 1 == 1 else "NO"
    print(res)
