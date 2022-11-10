n = int(input())
print("I hate", end="")
i = 1
while i < n:
    print(" that I ", end="")
    if i & 1 == 1:
        print("love", end="")
    else:
        print("hate", end="")
    i += 1
print(" it")
