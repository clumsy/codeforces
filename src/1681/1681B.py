t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    _, b = input(), (int(i) for i in input().split())
    j = sum(b) % n
    res = next(x for i, x in enumerate(a) if i == j)
    print(res)
