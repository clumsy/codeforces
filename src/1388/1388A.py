t = int(input())
for _ in range(t):
    n = int(input())
    if n > 30:
        print("YES")
        adjust = n - 30 in [6, 10, 14]
        print(6, 10, 14 + int(adjust), n - 30 - int(adjust))
    else:
        print("NO")
