t = int(input())
for _ in range(t):
    a, b, c, d = (int(i) for i in input().split())
    print(sum(1 for i in (b, c, d) if i > a))
