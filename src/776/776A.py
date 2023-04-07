res = set(input().split())
n = int(input())
print(*res)
for _ in range(n):
    res.symmetric_difference_update(set(input().split()))
    print(*res)
