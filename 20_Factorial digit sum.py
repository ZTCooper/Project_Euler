from functools import reduce
result = reduce(lambda x,y: x*y, range(1,101))
#import math
#math.factorial(100)
ans = 0
for i in str(result):
    ans += int(i)
print(ans)
