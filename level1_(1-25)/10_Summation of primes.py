import time
import math

t1 = time.time()
ls = [2,3,]
i = 5
while i<2000000:
    if all(i%j != 0 for j in range(3,int(math.sqrt(i)+1),2)):
        ls.append(i)
    i += 2
print(sum(ls))

t2 = time.time()
print(t2-t1)
