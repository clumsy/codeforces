n = int(input())
t, c = [0] * n, [0] * n
for i in range(n):
    t[i], c[i] = (int(i) for i in input().split())
ord = sorted(range(n), key=t.__getitem__)
max_q = cur_q = cur_t = 0
for i in ord:
    cur_q = max(0, cur_q - (t[i] - cur_t)) + c[i]
    max_q = max(max_q, cur_q)
    cur_t = t[i]
res = cur_t + cur_q, max_q
print(*res)
