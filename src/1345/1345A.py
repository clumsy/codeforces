t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = "YES" if n == 1 or m == 1 or (n == 2 and m == 2) else "NO"
    print(res)
