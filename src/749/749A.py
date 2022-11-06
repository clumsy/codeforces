n = int(input())
res = [2 for _ in range(n // 2)]
if n & 1 == 1:
    res[-1] += 1
print(len(res))
print(*res)
