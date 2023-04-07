t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    # |OB - AB| == k
    # case 1: OB > AB => OB - AB = k
    # either 0 < B < A => OA = OB + AB => n + k = 2OB => OB = (n + k)/2
    # or 0 < A < B => OB = OA + AB => OB = n + AB => OB + k = n + OB => n = k - any OB
    # case 2: AB > OB => AB - OB = k
    # implies 0 < B < A => OA = OB + AB => n + k = 2AB => AB = (n + k)/2 => OB = (n - k)/2
    res = (n - k) & 1 if n > k else k - n
    print(res)
