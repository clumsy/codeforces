t = int(input())
for _ in range(t):
    rating = int(input())
    if rating >= 1900:
        x = 1
    elif rating >= 1600:
        x = 2
    elif rating >= 1400:
        x = 3
    else:
        x = 4
    print(f"Division {x}")
