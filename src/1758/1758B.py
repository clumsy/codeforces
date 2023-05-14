t = int(input())
for _ in range(t):
    n = int(input())
    if n & 1 == 1:
        # 1 ^ 1 ^ ... ^ 1 ^ x = (n - 1 + x)/n
        # n*x = n - 1 + x => x = 1
        res = [1] * n
    else:
        # 2 ^ 2 ^ ... ^ x ^ y = (2n - 4 + x + y)/n
        # x ^ y * n = 2n - 4 + x + y => x, y = 1, 3 => 2n = 2n - 4 + 4
        res = [2] * (n - 2) + [1, 3]
    print(*res)
