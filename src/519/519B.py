n = int(input())
a = sum(int(i) for i in input().split())
b = sum(int(i) for i in input().split())
c = sum(int(i) for i in input().split())
res = a - b, b - c
print(*res, sep="\n")
