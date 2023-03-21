x = int(input())
hh, mm = (int(i) for i in input().split())
h, m = hh, mm
res = 0
while h % 10 != 7 and m % 10 != 7:
    res += 1
    mins = x * res
    h = (hh - mins // 60 - (mins % 60 > mm)) % 24
    m = (mm - mins) % 60
print(res)
