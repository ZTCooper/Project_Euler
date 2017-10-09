ls = [1,2]
ans = 2
while ls[-1] < 4000000:
    ls.append(ls[-1]+ls[-2])
    if ls[-1]%2 == 0:
        ans += ls[-1]
print(ans)
