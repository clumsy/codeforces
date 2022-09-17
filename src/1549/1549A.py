t = int(input())
for _ in range(t):
    P = int(input())
    # since P is prime it's odd, hence P - 1 is even
    # P mod (P - 1) = P mod 2 = 1
    res = 2, P - 1
    print(*res)
