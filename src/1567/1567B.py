def xor(n):
    return [n, 1, n + 1, 0][n % 4]


t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    x = 0 ^ xor(a - 1)
    res = a + 2 if x ^ b == a else a + 1 if x != b else a
    print(res)
