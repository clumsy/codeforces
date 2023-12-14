r1, c1, r2, c2 = (int(i) for i in input().split())
r = 0 if r1 == r2 and c1 == c2 else 1 if r1 == r2 or c1 == c2 else 2
b = (
    0
    if r1 + c1 & 1 != r2 + c2 & 1 and r1 - c1 != r2 - c2
    else 1
    if r1 - c1 == r2 - c2 or r1 + c1 == r2 + c2
    else 2
)
dr, dc = abs(r1 - r2), abs(c1 - c2)
k = (min(dr, dc) + 1) // 2 + max(dr, dc) - (min(dr, dc) + 1) // 2
res = r, b, k
print(*res)
