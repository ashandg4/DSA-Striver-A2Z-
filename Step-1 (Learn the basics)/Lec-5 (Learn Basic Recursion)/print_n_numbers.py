# Recursion syntax
count = 0


def f():
    global count
    if count == 8:
        return
    print(count)
    count += 1
    f()


f()
