t = int(input())
for _ in range(t):
    n = int(input())
    if n & 1 == 1:
        print("NO")
    else:
        print("YES")
        res = "AABB" * (n // 4) + "AABB"[: n % 4]
        print(res)
