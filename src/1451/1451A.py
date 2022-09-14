t = int(input())
for _ in range(t):
    n = int(input())
    # always n - 1 for n < 4
    # always 2 for even n > 2: n -> 2 -> 1
    # always 3 for odd n > 3: n -> n - 1 -> 2 -> 1
    res = n - 1 if n < 4 else 2 if n & 1 == 0 else 3
    print(res)
