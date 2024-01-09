hh, mm = (int(i) for i in input().split())
h, d, c, n = (int(i) for i in input().split())
mins = hh * 60 + mm
min_bfr = max(0, 20 * 60 - mins)
bfr = (h + n - 1) // n
afr = (h + d * min_bfr + n - 1) // n
res = min(c * bfr, 0.8 * c * afr)
print(res)
