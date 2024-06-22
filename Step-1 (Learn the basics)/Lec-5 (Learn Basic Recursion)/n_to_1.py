def dsc(i, n):
    if i > n:
        return
    print(n)
    dsc(i, n-1)


dsc(1, 5)
