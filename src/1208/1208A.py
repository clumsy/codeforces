t = int(input())
for _ in range(t):
    a, b, n = (int(i) for i in input().split())
    # 011
    # 100
    # 111
    # 011
    # 100
    res = {
        0: a,
        1: b,
        2: a ^ b,
    }[n % 3]
    print(res)
