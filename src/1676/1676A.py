n = int(input())
for _ in range(n):
    d = list(map(int, iter(input())))
    print("YES" if sum(d[0:3]) == sum(d[3:]) else "NO")
