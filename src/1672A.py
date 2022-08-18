t = int(input())
for _ in range(t):
    _, a = input(), (int(x) for x in input().split())
    # no matter how we cut log of length x will be cut in x - 1 pieces
    s = sum(x - 1 for x in a)
    print("errorgorn" if s & 1 == 1 else "maomao90")
