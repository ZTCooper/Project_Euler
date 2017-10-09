def d(n):
    sum1 = 0
    for i in range(2,int(n**.5+1)):
        if n%i == 0:
            sum1 = sum1 + i
            if i != n**.5:
                sum1 += n/i
    return sum1+1


abundants = set(i for i in range(1,28124) if d(i)>i)

def found(i):
    return any(i-a in abundants for a in abundants)        #若能写为两个abundant的和，则return True

print(sum(i for i in range(1,28124) if not found(i)))

