from math import sqrt

H, L = (int(i) for i in input().split())
D_2 = H**2 + L**2
# (Heron formula) (A + D/2)(D/2)*(D/2)*(A - D/2) = (A*L/2)^2 (trinagle area)
# D^2 * (A^2 - D^2/4) = A^2 * L^2
# A^2 = (D^4)/4(D^2 - L^2)
A = sqrt(D_2**2 / (4 * (D_2 - L**2)))
res = A - H
print(res)
