t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    if n & 1 == 1:
        for i in range(3, n + 1):
            if n % i == 0:
                n += i
                k -= 1
                break
    res = n + 2 * k
    print(res)
