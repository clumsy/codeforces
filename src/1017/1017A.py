n = int(input())
t, res = -1, 1
for _ in range(n):
    s = sum(int(i) for i in input().split())
    if t < 0:
        t = s
    elif s > t:
        res += 1
print(res)
