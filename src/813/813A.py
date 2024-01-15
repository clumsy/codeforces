n = int(input())
a = (int(i) for i in input().split())
need = sum(a)
m = int(input())
res = -1
for _ in range(m):
    lo, hi = (int(i) for i in input().split())
    if lo >= need:
        res = lo
        break
    elif lo <= need <= hi:
        res = need
        break
print(res)
