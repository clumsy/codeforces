n = int(input())
# first value won't be compared to all others
res = [-1] if n < 3 else ([2, 2] + [1] * (n - 2))
print(*res)
