t = int(input())
for _ in range(t):
    n = int(input())
    rem = n % 7
    if rem == 0:
        print(n)
        continue
    res = n + 7 - rem if rem >= n % 10 else n - rem
    print(res)
