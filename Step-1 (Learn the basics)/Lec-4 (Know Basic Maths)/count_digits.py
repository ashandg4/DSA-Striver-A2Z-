N = 22074
a = 0
b = N
lst = []

while N > 0:
    a = N % 10
    N //= 10
    lst.append(a)

lst2 = []
for i in lst[::-1]:
    if i != 0:
        if b % i == 0:
            lst2.append(i)

print(len(lst2))
