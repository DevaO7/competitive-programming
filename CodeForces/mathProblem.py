# https://codeforces.com/problemset/problem/1227/A
# Difficulty Level - 7/10 (1/1/2022)
def logicOne(a1, b1, a2, b2, phi):
    if b1 < min(a2, b2):
        commSeg = [b1, a2]
        phi = 1
    if b2 < min(a1, b1):
        commSeg = [b2, a1]
        phi = 1
    if a2 <= a1 <= b2:
        if b1 <= b2:
            commSeg = [a1, b1]
        if b1 > b2:
            commSeg = [a1, b2]
    if a1 <= a2 <= b1:
        if b2 <= b1:
            commSeg = [a2, b2]
        else:
            commSeg = [a2, b1]
    a1, b1 = commSeg[0], commSeg[1]
    return a1, b1, phi


def logicTwo(a1, b1, a2, b2):
    if a2 > b1:
        commSeg = [a1, a2]
    elif a1 > b2:
        commSeg = [b2, b1]
    else:
        commSeg = [a1, b1]
    a1, b1 = commSeg[0], commSeg[1]
    return a1, b1


t = int(input())
for i in range(t):
    n = int(input())
    phi = 0
    Ax = input().split()
    a1 = int(Ax[0])
    b1 = int(Ax[1])
    if n == 1:
        print(0)
        continue
    for i in range(n-1):
        Ay = input().split()
        a2 = int(Ay[0])
        b2 = int(Ay[1])
        if phi == 0:
            a1, b1, phi = logicOne(a1, b1, a2, b2, phi)
        else:
            a1, b1 = logicTwo(a1, b1, a2, b2)
    if phi == 0:
        print(0)
    else:
        print(b1-a1)
