q = int(input())
for _ in range(q):
    l, r = (int(i) for i in input().split())
    c = r - l + 1
    res = ((-1) ** (1 - (l & 1))) * (c // 2)
    if c & 1 == 1:
        res += ((-1) ** (r & 1)) * r
    print(res)
