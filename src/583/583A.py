n = int(input())
v_done, h_done = [False] * n, [False] * n
res = []
for i in range(n**2):
    v, h = (int(i) for i in input().split())
    if not v_done[v - 1] and not h_done[h - 1]:
        res.append(i + 1)
        v_done[v - 1] = h_done[h - 1] = True
print(*res)
