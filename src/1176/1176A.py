q = int(input())
for _ in range(q):
    n = int(input())
    res = 0
    while n > 1:
        if n % 2 == 0:
            res += 1
            n //= 2
        elif n % 3 == 0:
            res += 2
            n //= 3
        elif n % 5 == 0:
            res += 3
            n //= 5
        else:
            break
    res = -1 if n != 1 else res
    print(res)
