# (xv + yu)*(u + v) = (x + y)* uv
# xuv + xv^2 + yuv + yu^2 = xuv + yuv
# xv^2 + yu^2 = 0
# y = -xv^2/u^2
# x | u^2 => x = u^2
t = int(input())
for _ in range(t):
    u, v = (int(i) for i in input().split())
    x, y = u**2, -(v**2)
    print(x, y)
