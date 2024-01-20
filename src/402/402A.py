k, a, b, v = (int(i) for i in input().split())
need = (a + v - 1) // v
res, rem = divmod(min(need, b), k - 1)
res = min(res, (need + k - 1) // k)
left = max(0, need - k * res)
if left and rem:
    left = max(0, left - (rem + 1))
    res += 1
res += left
print(res)
