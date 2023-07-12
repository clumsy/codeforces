t = int(input())
for _ in range(t):
    n = int(input())
    c = (3 * n) // 4  # all digits are 9s: 1001
    res = "9" * c + "8" * (n - c)
    print(res)
