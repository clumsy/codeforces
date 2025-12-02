t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = n - s.count(s[-1])
    print(res)
