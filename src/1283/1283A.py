t = int(input())
for _ in range(t):
    h, m = (int(i) for i in input().split())
    res = (23 - h) * 60 + (60 - m)
    print(res)
