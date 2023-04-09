hh, mm = (int(i) for i in input().split(":"))
a = int(input())
dh, mm = divmod(mm + a, 60)
hh = (hh + dh) % 24
res = f"{hh:02d}:{mm:02d}"
print(res)
