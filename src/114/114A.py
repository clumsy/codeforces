k, L = (int(input()) for _ in range(2))
res = 0
while L > k:
    L /= k
    res += 1
if L == k:
    print("YES")
    print(res)
else:
    print("NO")
