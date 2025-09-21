t = int(input())
for _ in range(t):
    x, n = (int(i) for i in input().split())
    res = 0 if n & 1 == 0 else x
    print(res)
