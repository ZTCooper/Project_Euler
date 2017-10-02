import datetime
import math

t1 = datetime.datetime.now()
ls = [2,3,]
i = 5
while len(ls)<10001:
    if all(i%j != 0 for j in range(3,int(math.sqrt(i)+1),2)):
        ls.append(i)
    i += 2
print(ls[-1])

t2 = datetime.datetime.now()
print(t2-t1)
