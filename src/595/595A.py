n, m = (int(i) for i in input().split())
res = 0
for _ in range(n):
    floor = [int(i) for i in input().split()]
    flats = [floor[2 * i : 2 * i + 2] for i in range(m)]
    res += sum(1 for f, s in flats if f + s > 0)
print(res)
