n = int(input())
a = (int(i) for i in input().split())
res = [n - i + 1 for i in a]
print(*res)
