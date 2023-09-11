n, a = int(input()), sorted(int(i) for i in input().split())
res = (n - 1) // 2
print(res)
res = [i for hi, lo in zip(a[res:], a[:res]) for i in (hi, lo)] + (
    [a[-1]] if n & 1 == 1 else a[-2:]
)
print(*res)
