t = int(input())
for _ in range(t):
    n = int(input())
    # 2 is the smallest factor for composite number,
    # so n // 2 is the maximum one, and it's < n
    res = n // 2
    print(res)
