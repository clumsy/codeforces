t = int(input())
for _ in range(t):
    k = int(input())
    d = [0] + [int(i) for i in input().split()]
    print("YES" if d[k] > 0 and d[d[k]] > 0 else "NO")
