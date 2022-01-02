t = int(input())


def costToSave(x, n):
    return n-x


def merge(L, R):
    l = len(L)
    r = len(R)
    arr = []
    left = 0
    right = l - 1
    while (left + right < l+r):
        pass


def mergeSort(arr):
    n = len(arr)
    if n == 1:
        return arr
    L = mergeSort(arr[:n//2])
    R = mergeSort(arr[n//2:])
    return merge(L, R)


for i in range(t):
    temp = input().split()
    totalCost = 0
    costArray = []
    n = int(temp[0])
    array = [int(j) for j in input().split()]
    for j in array:
        totalCost += costToSave(j, n)
        costArray.append(costToSave(j, n))
    if totalCost <= n:
        print(len(array))
    else:
