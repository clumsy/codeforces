t = int(input())
for _ in range(t):
    n = int(input())
    num = str(n)
    res = 9 * (len(num) - 1) + int(num[0]) - (n < int(num[0] * len(num)))
    print(res)
