n = int(input())
a = (int(i) for i in input().split())
b = sorted(int(i) for i in input().split())
res = "YES" if sum(a) <= sum(b[-2:]) else "NO"
print(res)
