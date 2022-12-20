n = int(input())
pos = 0
for _ in range(n):
    x, _ = (int(i) for i in input().split())
    pos += x > 0
res = "YES" if pos < 2 or n - pos < 2 else "NO"
print(res)
