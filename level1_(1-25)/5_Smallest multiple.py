import datetime
t1 = datetime.datetime.now()

i = 380
while True:
    if all(i%j ==0 for j in range(1,21)):
        ans = i
        break
    else:
        i += 380    #优化后
print(ans)

t2 = datetime.datetime.now()
print(t2-t1)
