t = int(input())
for _ in range(t):
    n, m, sx, sy, d = (int(i) for i in input().split())
    # check if we can walk along either edge
    down_and_right = min(abs(n - sx), sy - 1) > d
    right_and_down = min(abs(m - sy), sx - 1) > d
    res = n - 1 + m - 1 if down_and_right or right_and_down else -1
    print(res)
