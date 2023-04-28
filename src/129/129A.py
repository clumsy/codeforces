n, a = int(input()), (int(i) for i in input().split())
res = even = odd = 0
for i in a:
    res += i
    even += 1 - (i & 1)
    odd += i & 1
res = even if res & 1 == 0 else odd
print(res)
