t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    # if the sum is even -> it can be represented as a sum of two even or odd, so YES
    res = "YES" if sum(a) & 1 == 0 else "NO"
    print(res)
