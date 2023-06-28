q = int(input())
for _ in range(q):
    l, r, d = (int(i) for i in input().split())
    res = d if d < l else d * ((r + d - 1) // d + (r % d == 0))
    print(res)
