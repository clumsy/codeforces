n = int(input())
h = [int(input()) for _ in range(n)]
res = cur = 0
for i in range(n):
    res += h[i] - cur + 1  # 1 to eat
    if i < n - 1:
        res += max(0, h[i] - h[i + 1]) + 1  # 1 to jump
        cur = min(h[i], h[i + 1])
print(res)
