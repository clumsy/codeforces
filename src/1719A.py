t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    # if rows and cols are both even or odd first player loses, else always wins
    print("Tonya" if sum([n & 1, m & 1]) & 1 == 0 else "Burenka")
