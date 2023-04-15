h, m = (int(i) for i in input().split(":"))
dh, dm = (int(i) for i in input().split(":"))
h -= dh
m -= dm
if m < 0:
    h -= 1
    m += 60
h %= 24
res = f"{h:02}:{m:02}"
print(res)
