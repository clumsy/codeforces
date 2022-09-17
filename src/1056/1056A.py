n = int(input())
res = set(range(1, 101))
for _ in range(n):
    r, *lines = (int(i) for i in input().split())
    res &= set(lines)
print(*res)
