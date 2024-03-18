t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    xk, yk = (int(i) for i in input().split())
    dxy = ((a, b), (-a, b), (a, -b), (-a, -b), (b, a), (-b, a), (b, -a), (-b, -a))
    k = {(xk + dx, yk + dy) for dx, dy in dxy}
    xq, yq = (int(i) for i in input().split())
    q = {(xq + dx, yq + dy) for dx, dy in dxy}
    res = len(k & q)
    print(res)
