def bubbleSort(nlist):
    n = len(nlist)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nlist[j] > nlist[j + 1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
    return nlist
