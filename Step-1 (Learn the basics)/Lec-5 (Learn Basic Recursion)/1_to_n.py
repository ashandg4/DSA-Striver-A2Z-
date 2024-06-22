def inc(i, n):
    if i > n:
        return
    print(i)
    inc(i+1, n)


inc(1, 10)
