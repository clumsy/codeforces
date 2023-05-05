n = int(input())


def solve(a, b):
    a, b = min(a, b), max(a, b)
    if a == 0:
        return 0
    if a == b:
        return 1
    d, r = divmod(b, a)
    return d + solve(r, a)


for _ in range(n):
    a, b = (int(i) for i in input().split())
    res = solve(a, b)
    print(res)
