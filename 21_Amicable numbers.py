def d(n):
    sum1 = 0
    for i in range(2,int(n**.5+1)):     #这里进行优化
        if n%i == 0:
            sum1 = sum1 + i
            if i != n**.5:
                sum1 += n/i
    return sum1+1

sum2 = 0
for x in range(1,10000):
    if x == d(d(x)) and x != d(x):
        sum2 += x
print(sum2)

