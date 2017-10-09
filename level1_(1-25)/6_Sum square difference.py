'''m = sum([x*x for x in range(1,101)])
n = sum([x for x in range(1,101)])**2
print(abs(m-n))
'''
print(abs(sum([x*x for x in range(1,101)])-sum([x for x in range(1,101)])**2))
