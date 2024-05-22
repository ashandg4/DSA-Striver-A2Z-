N = 6
ans = 0

for i in range(1, N+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += j
    ans += count
print(ans)
