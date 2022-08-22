import math

t = int(input())
for _ in range(t):

    def is_integer(n):
        return n == int(n)

    x, y = (int(i) for i in input().split())
    if (x, y) == (0, 0):
        print("0")  # already there
    elif is_integer(math.sqrt(x**2 + y**2)):
        print("1")  # can go directly
    else:
        print("2")  # we can always move to (x, 0) and then to (x, y)
