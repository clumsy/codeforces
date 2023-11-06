l, r = (int(i) for i in input().split())
res = (
    range(l, l + 3)
    if l & 1 == 0 and r - l > 1
    else range(l + 1, l + 4)
    if r - l > 2
    else [-1]
)
print(*res)
