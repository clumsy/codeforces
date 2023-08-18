t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = [n - i // 2 if i & 1 == 0 else i // 2 + 1 for i in range(n)]
    print(*res)
