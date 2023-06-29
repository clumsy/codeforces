s, e = (input() for _ in range(2))
h1, m1 = (int(i.lstrip("0") or 0) for i in s.split(":"))
h2, m2 = (int(i.lstrip("0") or 0) for i in e.split(":"))
time = (60 * (h2 + h1) + (m2 + m1)) // 2
res = divmod(time, 60)
res = f"{res[0]:02d}:{res[1]:02d}"
print(res)
