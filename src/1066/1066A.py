t = int(input())
for _ in range(t):
    L, v, le, ri = (int(i) for i in input().split())
    res = L // v - (ri // v - (le - 1) // v)
    print(res)
