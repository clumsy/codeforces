n, m = (int(i) for i in input().split())
s, t, q = input().split(), input().split(), int(input())
for _ in range(q):
    y = int(input())
    res = s[(y - 1) % n] + t[(y - 1) % m]
    print(res)
