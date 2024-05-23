t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    mapie, map, pie = (s.count(p) for p in ("mapie", "map", "pie"))
    res = map + pie - mapie
    print(res)
