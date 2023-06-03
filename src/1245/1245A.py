t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    # a=3, b=7
    # W B B W B B W W B W W  B  W  W  W
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

    a, b = sorted([a, b])
    res = "Infinite" if gcd(b, a) != 1 else "Finite"
    print(res)
