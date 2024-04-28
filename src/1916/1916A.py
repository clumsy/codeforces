t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    b = (int(i) for i in input().split())
    p, res = 1, "YES"
    for i in b:
        if i & 1 == 0:
            res = "NO"
        p *= i
    if p > 2023 or 2023 % p != 0:
        res = "NO"
    print(res)
    if res == "YES":
        res = [2023 // p] + [1] * (k - 1)
        print(*res)
