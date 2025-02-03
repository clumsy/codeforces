t = int(input())
for _ in range(t):
    l, r = (int(i) for i in input().split())
    res = 1 if l == r == 1 else r - l
    print(res)
