t = int(input())
for _ in range(t):
    l, r, k = (int(i) for i in input().split())
    total = r - l + 1
    # number of odd elements has to be <= k > => gcb(a) >= 2
    odd = (total + 1) // 2 if l & 1 == 1 else total // 2
    print("YES" if (total == 1 and l > 1) or odd <= k else "NO")
