from math import sqrt, floor


t = int(input())
for _ in range(t):
    l, r = (int(i) for i in input().split())
    l, r = 0, r - l
    # 0 + 1 + 2 + 3 + ... = (0 + a_y) * (y + 1) // 2 = r => (0 + 0 + 1 * y) * (y + 1) = 2 * r => y^2 + y = 2 * r
    res = floor((sqrt(1 + 8 * r) - 1) // 2) + 1
    print(res)
