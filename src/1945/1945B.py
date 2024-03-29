t = int(input())
for _ in range(t):
    a, b, m = (int(i) for i in input().split())
    res = (m + 1 + a - 1) // a + (m + 1 + b - 1) // b
    print(res)
