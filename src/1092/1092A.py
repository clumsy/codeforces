t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = "".join(chr(ord("a") + (i % k)) for i in range(n))
    print(res)
