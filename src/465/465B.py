n, a = int(input()), (int(i) for i in input().split())
res, prev = 0, None
for i in a:
    res += (1 + (res > 0 and prev != i)) if i == 1 else 0
    prev = i
print(res)
