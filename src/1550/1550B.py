t = int(input())
for _ in range(t):
    n, a, b = (int(i) for i in input().split())
    s = input()
    if b >= 0:
        res = (a + b) * n
    else:
        res = a * n + b * (max(s.count("10"), s.count("01")) + 1)
    print(res)
