import time
t1 = time.time()

count = 0
times = []
for n in range(1,1000000):
    while n != 1:
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        count += 1
    times.append(count)
    count = 0
print(times.index(max(times))+1)
  
t2 = time.time()
print(t2-t1)
