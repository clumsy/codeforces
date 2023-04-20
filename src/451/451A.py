n, m = (int(i) for i in input().split())
res = "Akshat" if min(n, m) & 1 == 1 else "Malvika"
print(res)
