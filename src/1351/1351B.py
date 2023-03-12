t = int(input())
for _ in range(t):
    ab1 = sorted(int(i) for i in input().split())
    ab2 = sorted(int(i) for i in input().split())
    res = "YES" if ab1[1] == ab2[1] == (ab1[0] + ab2[0]) else "NO"
    print(res)
