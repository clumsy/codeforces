n, c = (int(i) for i in input().split())
p = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
res, lim, rad = 0, 0, 0
for i in range(n):
    lim += t[i]
    j = n - 1 - i
    rad += t[j]
    res += max(0, p[i] - c * lim) - max(0, p[j] - c * rad)
res = "Tie" if res == 0 else "Limak" if res > 0 else "Radewoosh"
print(res)
