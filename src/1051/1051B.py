L, R = (int(i) for i in input().split())
print("YES")
while L < R:
    print(L, L + 1)
    L += 2
