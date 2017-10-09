ls = []
for i in range(100,1000):
    for j in range(100,1000):
        k = i * j
        if list(str(k)) == list(reversed(list(str(k)))):    #判断回文
            ls.append(k)
print(max(ls))
