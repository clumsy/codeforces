n = int(input())
for _ in range(n):
    s, a, b, c = (int(i) for i in input().split())
    k = s // c
    res = (k // a) * (a + b) + (k % a)
    print(res)
