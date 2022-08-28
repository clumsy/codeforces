t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    diff = min(a, b)
    mix, zeroes, ones = "01" * diff, "0" * (a - diff), "1" * (b - diff)
    print(mix + zeroes + ones)
