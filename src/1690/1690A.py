import math

t = int(input())
for _ in range(t):
    n = int(input())
    # minimal when h1=x, h2=x-1, h3=x-2, hence x+x-1+x-2=n => 3x-3=n => x=1+n/3
    h1 = math.ceil(1 + n / 3)
    # one possibility when h2=y, h3=y-1 where y+y-1=n-h1 => 2y-1=n-h1 => y=(n-h1+1)/2
    h2 = math.ceil((n - h1 + 1) / 2)
    # whatever is left
    h3 = n - h1 - h2
    print(h2, h1, h3)
