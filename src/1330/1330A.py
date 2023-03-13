t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    place = set()
    for i in a:
        place.add(i)
    i = 1
    while i in place or x:
        res = i
        x -= i not in place
        i += 1
    print(res)
