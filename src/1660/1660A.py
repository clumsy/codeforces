t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    # if a == 0 we cannot pay 1 burle
    # with just 1 burle we can get any price up to 2*b, then we can use all a burle
    print(1 if a == 0 else 2 * b + a + 1)
