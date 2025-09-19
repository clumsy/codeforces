t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    b = (int(i) for i in input().split())
    res = 1 + sum(max(0, ai - bi) for ai, bi in zip(a, b))
    print(res)
