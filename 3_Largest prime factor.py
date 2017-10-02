num = 600851475143
i = 3
while i <= num:
    if num%i == 0:
        num /= i
        ans = i
    i += 1

print(ans)
