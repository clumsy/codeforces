n = int(input())
d, r = divmod(n, 7)
while d:
    if r % 4 == 0:
        break
    d -= 1
    r += 7
res = "4" * (r // 4) + "7" * d
res = -1 if sum(int(i) for i in res) != n else res
print(res)
