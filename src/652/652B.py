from itertools import zip_longest

n, a = int(input()), sorted(int(i) for i in input().split())
mid = (n + 1) // 2
res = [i for x, y in zip_longest(a[:mid], a[mid:][::-1], fillvalue=0) for i in (x, y)]
if n & 1 == 1:
    res.pop()
print(*res)
