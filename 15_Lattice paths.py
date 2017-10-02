import time
t1 = time.time()

f = [[0 for i in range(21)] for i in range(21)]
for i in range(21):
    f[0][i] = f[i][0] =1
for i in range(1,21):
    for j in range(1,21):
        f[i][j] = f[i-1][j] + f[i][j-1]
print(f[20][20])

t2 = time.time()
print(t2-t1)
