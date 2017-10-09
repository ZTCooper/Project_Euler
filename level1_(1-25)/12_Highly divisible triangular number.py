import time
t1 = time.time()

def get_divisors(x):
    n = 0
    for i in range(1,int(x**.5+1)):
        if x%i == 0:
            n += 1
    return n*2      #*2得到约数个数

a = 1; i = 2
while True:
    a = a + i
    i += 1
    if get_divisors(a) > 500:
        print(a)
        break

t2 = time.time()
print(t2-t1)
