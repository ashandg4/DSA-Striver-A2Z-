def f(i, n):
    if i < 1:
        return
    f(i-1, n)
    print(i)


f(5, 5)
