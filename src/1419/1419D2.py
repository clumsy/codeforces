n, a = int(input()), sorted(int(i) for i in input().split())
half = n // 2
arr = [i for hi, lo in zip(a[half:], a[:half]) for i in (hi, lo)] + (
    [a[-1]] if n & 1 == 1 else []
)
res = 0
for i in range(1, n - 1):
    res += arr[i - 1] > arr[i] < arr[i + 1]
print(res)
print(*arr)
