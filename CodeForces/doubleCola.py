# https://codeforces.com/problemset/problem/82/A
# Difficulty Level - 6/10 (1/1/2022)


import math


def getName(n):
    if n == 0:
        return 'Sheldon'
    if n == 1:
        return 'Leonard'
    if n == 2:
        return 'Penny'
    if n == 3:
        return 'Rajesh'
    if n == 4:
        return 'Howard'


N = int(input())
if N > 5:
    N = N-1
    x = math.modf(math.log2(N/5+1))[1]
    A = 5*(2**x-1)
    print(getName((N-A)//2**(x)))
else:
    print(getName(N-1))
