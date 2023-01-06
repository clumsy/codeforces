n = int(input())
res = 0
for _ in range(n):
    p, q = (int(i) for i in input().split())
    res += int(q - p > 1)
print(res)
