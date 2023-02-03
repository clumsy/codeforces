t = int(input())
for _ in range(t):
    n, c0, c1, h = (int(i) for i in input().split())
    s = input()
    _, ones = (zeros := s.count("0")), n - zeros
    res = min(
        zeros * c0 + ones * c1,
        n * c0 + h * ones,
        n * c1 + h * zeros,
    )
    print(res)
