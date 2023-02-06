t = int(input())
for _ in range(t):
    n = int(input())
    half = n // 2
    if half & 1 == 1:
        # sum of odd number of odd numbers is odd, first half is always even
        print("NO")
    else:
        print("YES")
        res = [0] * n
        res[:half] = list(range(2, n + 1, 2))
        res[half : n - 1] = list(range(1, 2 * half - 1, 2))
        res[-1] = sum(res[:half]) - sum(res[half : n - 1])
        print(*res)
