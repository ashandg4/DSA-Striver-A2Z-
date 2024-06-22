def f(i, n):
    if i < 1:
        return
    print(i)
    f(i-1, n)


f(5, 5)
