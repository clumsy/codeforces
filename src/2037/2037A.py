t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    s, res = set(), 0
    for i in a:
        if i in s:
            res += 1
            s.remove(i)
        else:
            s.add(i)
    print(res)
