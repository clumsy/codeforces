t = int(input())
for _ in range(t):
    n = int(input())
    res = max(n + (n & 1), 6) // 2 * 5
    print(res)
