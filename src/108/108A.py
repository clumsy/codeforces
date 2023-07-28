from bisect import bisect_left

s = input()
pal = [
    "00:00",
    "01:10",
    "02:20",
    "03:30",
    "04:40",
    "05:50",
    "10:01",
    "11:11",
    "12:21",
    "13:31",
    "14:41",
    "15:51",
    "20:02",
    "21:12",
    "22:22",
    "23:32",
]
i = bisect_left(pal, s)
n = len(pal)
res = pal[i % n] if pal[i % n] != s else pal[(i + 1) % n]
print(res)
